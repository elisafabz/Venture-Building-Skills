#!/usr/bin/env python3
"""Deploy a complete Meta Ad campaign from copy JSON + images + config.

Usage:
  python3 deploy_campaign.py --config campaign.json

Reads copy from the JSON file specified in config.copy_file,
uploads images, creates campaign → ad set → creatives → ads.
Everything is created PAUSED.

Requires: META_ACCESS_TOKEN and META_AD_ACCOUNT_ID in ~/.claude/.env
"""

import argparse, json, os, sys
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from urllib.parse import urlencode
import mimetypes

try:
    from dotenv import load_dotenv
    env_path = os.path.expanduser("~/.claude/.env")
    if os.path.exists(env_path):
        load_dotenv(env_path)
except ImportError:
    pass

API_VERSION = "v20.0"
BASE_URL = f"https://graph.facebook.com/{API_VERSION}"


def api_post(endpoint, data):
    """POST to Meta Marketing API with form-encoded data."""
    encoded = urlencode(data).encode()
    req = Request(f"{BASE_URL}/{endpoint}", data=encoded, method="POST")
    try:
        with urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except HTTPError as e:
        body = e.read().decode()
        print(f"API Error {e.code} on {endpoint}:", file=sys.stderr)
        try:
            err = json.loads(body)
            msg = err.get("error", {}).get("message", body)
            sub = err.get("error", {}).get("error_subcode", "?")
            print(f"  Message: {msg}", file=sys.stderr)
            print(f"  Subcode: {sub}", file=sys.stderr)
        except json.JSONDecodeError:
            print(f"  {body}", file=sys.stderr)
        sys.exit(1)


def upload_image(account_id, token, filepath):
    """Upload image and return image_hash."""
    import subprocess
    result = subprocess.run([
        "curl", "-s",
        "-F", f"filename=@{filepath}",
        "-F", f"access_token={token}",
        f"{BASE_URL}/{account_id}/adimages"
    ], capture_output=True, text=True)

    resp = json.loads(result.stdout)
    if "images" in resp:
        # Response format: {"images": {"filename": {"hash": "..."}}}
        for fname, data in resp["images"].items():
            return data["hash"]
    print(f"ERROR uploading {filepath}: {resp}", file=sys.stderr)
    sys.exit(1)


def create_campaign(account_id, token, config):
    """Create a campaign, return campaign_id."""
    c = config["campaign"]
    data = {
        "name": c["name"],
        "objective": c["objective"],
        "status": "PAUSED",
        "special_ad_categories": json.dumps(c.get("special_ad_categories", [])),
        "is_adset_budget_sharing_enabled": json.dumps(c.get("is_adset_budget_sharing_enabled", False)),
        "access_token": token,
    }
    resp = api_post(f"{account_id}/campaigns", data)
    return resp["id"]


def create_ad_set(account_id, token, campaign_id, config):
    """Create an ad set, return adset_id."""
    s = config["ad_set"]
    data = {
        "name": s["name"],
        "campaign_id": campaign_id,
        "daily_budget": s["daily_budget_cents"],
        "optimization_goal": s["optimization_goal"],
        "billing_event": s["billing_event"],
        "bid_strategy": s["bid_strategy"],
        "targeting": json.dumps(s["targeting"]),
        **({"promoted_object": json.dumps(s["promoted_object"])} if s.get("promoted_object") else {}),
        "status": "PAUSED",
        "access_token": token,
    }
    if s.get("start_time"):
        data["start_time"] = s["start_time"]
    if s.get("end_time"):
        data["end_time"] = s["end_time"]

    # Placements
    if s.get("publisher_platforms"):
        data["publisher_platforms"] = json.dumps(s["publisher_platforms"])
    if s.get("facebook_positions"):
        data["facebook_positions"] = json.dumps(s["facebook_positions"])
    if s.get("instagram_positions"):
        data["instagram_positions"] = json.dumps(s["instagram_positions"])

    resp = api_post(f"{account_id}/adsets", data)
    return resp["id"]


def create_creative(account_id, token, config, angle, image_hash, angle_idx, variant, copy_data):
    """Create an ad creative with contextual_multi_ads, return creative_id."""
    ads_config = config["ads"]
    name = ads_config["naming_pattern"].format(angle=angle_idx + 1, variant=variant)

    # Primary text: use the configured type as main, rest as alternatives
    pref_type = config.get("primary_text_type", "medium")
    main_text = None
    alt_texts = []
    for pt in angle["primary_texts"]:
        if pt["type"] == pref_type and main_text is None:
            main_text = pt["text"]
        else:
            alt_texts.append(pt["text"])

    if main_text is None:
        main_text = angle["primary_texts"][0]["text"]
        alt_texts = [pt["text"] for pt in angle["primary_texts"][1:]]

    # Headlines: first as main, rest as alternatives
    main_headline = angle["headlines"][0]["text"]
    alt_headlines = [h["text"] for h in angle["headlines"][1:]]

    # Description
    description = angle.get("description", "")

    # Build contextual_multi_ads for alternative texts
    max_alt_hl = config.get("max_alt_headlines", 4)
    max_alt_pt = config.get("max_alt_primary_texts", 4)

    contextual_texts = []
    for h in alt_headlines[:max_alt_hl]:
        contextual_texts.append({"text": h, "text_type": "name"})
    for pt in alt_texts[:max_alt_pt]:
        contextual_texts.append({"text": pt, "text_type": "message"})

    creative_data = {
        "name": name,
        "object_story_spec": json.dumps({
            "page_id": ads_config["page_id"],
            "link_data": {
                "image_hash": image_hash,
                "link": ads_config["link"],
                "message": main_text,
                "name": main_headline,
                "description": description,
                "call_to_action": {
                    "type": ads_config["cta_type"],
                    "value": {"link": ads_config["link"]}
                }
            }
        }),
        "access_token": token,
    }

    if contextual_texts:
        creative_data["contextual_multi_ads"] = json.dumps({
            "enroll_status": "OPT_IN",
            "contextual_texts": contextual_texts
        })

    resp = api_post(f"{account_id}/adcreatives", creative_data)
    return resp["id"]


def create_ad(account_id, token, adset_id, creative_id, name):
    """Create an ad (PAUSED), return ad_id."""
    data = {
        "name": name,
        "adset_id": adset_id,
        "creative": json.dumps({"creative_id": creative_id}),
        "status": "PAUSED",
        "access_token": token,
    }
    resp = api_post(f"{account_id}/ads", data)
    return resp["id"]


def main():
    p = argparse.ArgumentParser(description="Deploy Meta Ad campaign from config + copy JSON")
    p.add_argument("--config", required=True, help="Path to campaign config JSON")
    p.add_argument("--dry-run", action="store_true", help="Print what would be created without calling API")
    args = p.parse_args()

    # Load credentials
    token = os.environ.get("META_ACCESS_TOKEN")
    account_id = os.environ.get("META_AD_ACCOUNT_ID")
    if not token:
        print("ERROR: META_ACCESS_TOKEN not set", file=sys.stderr)
        sys.exit(1)
    if not account_id:
        print("ERROR: META_AD_ACCOUNT_ID not set", file=sys.stderr)
        sys.exit(1)

    # Load config
    with open(args.config) as f:
        config = json.load(f)

    # Load copy
    copy_path = config["copy_file"]
    if not os.path.isabs(copy_path):
        copy_path = os.path.join(os.path.dirname(args.config), copy_path)
    with open(copy_path) as f:
        copy_data = json.load(f)

    angles = copy_data["angles"]
    use_indices = config.get("angles_to_use", list(range(len(angles))))
    selected = [angles[i] for i in use_indices if i < len(angles)]

    print(f"Campaign: {config['campaign']['name']}")
    print(f"Angles: {len(selected)} of {len(angles)}")
    print(f"Budget: {config['ad_set']['daily_budget_cents'] / 100:.0f} EUR/day")
    print(f"Optimization: {config['ad_set']['optimization_goal']}")
    print()

    if args.dry_run:
        print("=== DRY RUN ===\n")
        for i, idx in enumerate(use_indices):
            if idx >= len(angles):
                continue
            angle = angles[idx]
            ad_name = config["ads"]["naming_pattern"].format(angle=idx + 1, variant=0)
            print(f"Ad: {ad_name}")
            print(f"  Angle: {angle['name']}")
            print(f"  Main Headline: {angle['headlines'][0]['text']}")
            print(f"  Alt Headlines: {len(angle['headlines']) - 1}")
            pref = config.get("primary_text_type", "medium")
            main_pt = next((pt for pt in angle["primary_texts"] if pt["type"] == pref), angle["primary_texts"][0])
            print(f"  Main Text ({main_pt['type']}): {main_pt['text'][:80]}...")
            print(f"  Alt Texts: {len(angle['primary_texts']) - 1}")

            # Check for images
            img_dir = config["creatives"]["image_dir"]
            sq_path = os.path.join(img_dir, config["creatives"]["formats"]["square"], f"{idx + 1}.0_{config['creatives']['formats']['square']}.png")
            print(f"  Square: {'FOUND' if os.path.exists(sq_path) else 'MISSING'} ({sq_path})")
            vert_path = os.path.join(img_dir, config["creatives"]["formats"]["vertical"], f"{idx + 1}.0_{config['creatives']['formats']['vertical']}.png")
            print(f"  Vertical: {'FOUND' if os.path.exists(vert_path) else 'MISSING'} ({vert_path})")
            print()

        print("Vertical (9:16) images must be added MANUALLY in Ads Manager after deployment.")
        print("\nRun without --dry-run to deploy.")
        return

    # === DEPLOY ===
    print("1/5 Creating campaign...")
    campaign_id = create_campaign(account_id, token, config)
    print(f"     Campaign: {campaign_id}")

    print("2/5 Creating ad set...")
    adset_id = create_ad_set(account_id, token, campaign_id, config)
    print(f"     Ad Set: {adset_id}")

    # Upload images and create ads
    results = []
    img_dir = config["creatives"]["image_dir"]
    sq_subdir = config["creatives"]["formats"]["square"]
    vert_subdir = config["creatives"]["formats"]["vertical"]

    for i, idx in enumerate(use_indices):
        if idx >= len(angles):
            continue
        angle = angles[idx]
        ad_name = config["ads"]["naming_pattern"].format(angle=idx + 1, variant=0)

        # Find square image
        sq_filename = f"{idx + 1}.0_{sq_subdir}.png"
        sq_path = os.path.join(img_dir, sq_subdir, sq_filename)

        if not os.path.exists(sq_path):
            print(f"WARNING: Image not found: {sq_path} — skipping angle {idx + 1}", file=sys.stderr)
            continue

        print(f"3/5 Uploading image for {ad_name}...")
        image_hash = upload_image(account_id, token, sq_path)
        print(f"     Hash: {image_hash}")

        print(f"4/5 Creating creative for {ad_name}...")
        creative_id = create_creative(account_id, token, config, angle, image_hash, idx, 0, copy_data)
        print(f"     Creative: {creative_id}")

        print(f"5/5 Creating ad {ad_name}...")
        ad_id = create_ad(account_id, token, adset_id, creative_id, ad_name)
        print(f"     Ad: {ad_id}")

        # Check for vertical image
        vert_filename = f"{idx + 1}.0_{vert_subdir}.png"
        vert_path = os.path.join(img_dir, vert_subdir, vert_filename)
        vert_exists = os.path.exists(vert_path)

        results.append({
            "ad_name": ad_name,
            "ad_id": ad_id,
            "creative_id": creative_id,
            "angle": angle["name"],
            "square_image": sq_path,
            "vertical_image": vert_path if vert_exists else "MISSING",
            "vertical_manual": not vert_exists or True,  # Always manual due to API limit
        })
        print()

    # === SUMMARY ===
    print("=" * 60)
    print("DEPLOYMENT COMPLETE — all PAUSED")
    print("=" * 60)
    print(f"\nCampaign ID: {campaign_id}")
    print(f"Ad Set ID:   {adset_id}")
    print(f"Ads created: {len(results)}")

    # Manual steps table
    print("\n## MANUAL STEP: assign vertical (9:16) images")
    print("\nIn Ads Manager, open each ad → Media → Vertical → Replace:\n")
    print(f"| Ad | Ad ID | Vertical Bild |")
    print(f"|-----|-------|--------------|")
    for r in results:
        vert = r["vertical_image"]
        print(f"| {r['ad_name']} | {r['ad_id']} | {vert} |")

    print("\nThen set the ad set to ACTIVE.")

    # Save results
    results_path = args.config.replace(".json", "_results.json")
    with open(results_path, "w") as f:
        json.dump({
            "campaign_id": campaign_id,
            "adset_id": adset_id,
            "ads": results,
        }, f, ensure_ascii=False, indent=2)
    print(f"\nResults saved to {results_path}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAborted.")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)
