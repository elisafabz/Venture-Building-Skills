#!/usr/bin/env python3
"""Generate Meta Ad copy (hooks, primary texts, headlines) via Gemini API.

Usage:
  python3 generate_copy.py \
    --brand "yourbrand" \
    --product "AI-powered relationship companion for long-term couples" \
    --tone "measured, assured, elegant - calm, premium, human" \
    --audience "couples 25-45 in long-term relationships who want to strengthen it day to day" \
    --cta "Get started" \
    --language "English (UK)" \
    --angles 5 \
    --output copy_output.md

Requires: GEMINI_API_KEY in the environment or in ~/.claude/.env
"""

import argparse, os, sys, json

# Load .env
# Load .env from canonical location
try:
    from dotenv import load_dotenv
    # Primary: skill-level .env
    env_path = os.path.expanduser("~/.claude/.env")
    if os.path.exists(env_path):
        load_dotenv(env_path)
except ImportError:
    pass  # dotenv not installed, rely on environment variables

import google.generativeai as genai

def build_prompt(args):
    brand_voice_section = ""
    if hasattr(args, 'brand_voice') and args.brand_voice and os.path.exists(args.brand_voice):
        with open(args.brand_voice, "r") as f:
            brand_voice_section = f"\n## Brand voice specification (follow STRICTLY)\n\n{f.read()}\n"

    prompt = f"""You are an elite performance marketing copywriter with 15+ years in D2C and app marketing. You write copy that converts — not copy that "sounds nice".

## Your brief

Produce a complete Meta ad copy set for:

- **Brand:** {args.brand}
- **Product:** {args.product}
- **Tone of voice:** {args.tone}
- **Audience:** {args.audience}
- **CTA:** {args.cta}
- **Language:** {args.language}
{brand_voice_section}
## What you must deliver

### 1. Hook angles ({args.angles} of them)

Each hook from a different psychological perspective:
1. **Pain point** — a pain the audience feels every day
2. **Desire / aspiration** — paint the desired state emotionally
3. **Curiosity gap** — open a knowledge gap that compels the click
4. **Social proof / statistic** — lead with evidence or a number
5. **Pattern interrupt / contrarian** — break the expectation, provoke

For each hook: two variants (one as a question, one as a statement).

### 2. Primary texts (for each hook angle)

Four variants per hook:
- **Short (2-3 sentences):** hook plus CTA. Hard-hitting.
- **Medium (4-6 sentences):** hook → pain/desire → solution → CTA
- **Long story (8-12 sentences):** an emotional story arc. Open with "you know that feeling when...".
- **Long proof (8-12 sentences):** benefit stack plus social proof plus authority

### 3. Headlines (5 per hook)

255 characters max. Types: benefit, curiosity, social proof, urgency, question.

### 4. Description (1 per hook)

1-2 sentences, complementary, not redundant.

## Copy rules (follow STRICTLY)

- **The first sentence is the hook.** It decides whether they tap "see more". Make it irresistible.
- **Specific beats generic.** "Communicate better" is weak. "Understand what's really going on in five minutes" is strong.
- **Short sentences. Paragraphs. White space.** No walls of text.
- **Emotional before rational.** Feeling first, logic after.
- **No corporate speak.** No buzzwords. No filler. Write like a human.
- **No clickbait.** The headline must deliver what it promises.
- **No dark patterns.** No fake scarcity, no confirm-shaming.
- **Every piece of copy must be unique** — no repetition across variants.
- **Power words sparingly:** free, now, new, finally, without, instantly — and only where they fit.
- **MANDATORY: correct characters for the target language.** Always use the proper accents and diacritics of {args.language}. Never strip them (never write "Gruender" for "Gründer" or "francais" for "français"). Copy with stripped characters is NOT acceptable.

## Quality check before you hand over

Read every text again and ask yourself:
- Would I stop scrolling for this?
- Is the hook graspable within three seconds?
- Does it sound like a real person, or like AI slop?
- Is it specific enough for THIS product in particular?

If not, rewrite it.

## Output format

Return everything as structured Markdown. Per hook angle:

```
## Hook [N]: [angle name]

**Statement:** ...
**Question:** ...

### Primary texts
| # | Type | Text |
|---|------|------|

### Headlines
| # | Type | Text | Characters |
|---|------|------|------------|

### Description
...
```
"""

    json_instruction = ""
    if args.format == "json":
        json_instruction = """

## IMPORTANT: JSON output

Return the ENTIRE result as a single JSON object. No Markdown, no explanatory text — ONLY valid JSON.

Exact schema:

```json
{
  "brand": "Brand Name",
  "angles": [
    {
      "name": "Angle-Name",
      "hook_statement": "Statement-Hook...",
      "hook_question": "Question-hook...?",
      "primary_texts": [
        {"type": "short", "text": "..."},
        {"type": "medium", "text": "..."},
        {"type": "long_story", "text": "..."},
        {"type": "long_proof", "text": "..."}
      ],
      "headlines": [
        {"type": "benefit", "text": "...", "chars": 46},
        {"type": "curiosity", "text": "...", "chars": 52},
        {"type": "social_proof", "text": "...", "chars": 49},
        {"type": "urgency", "text": "...", "chars": 46},
        {"type": "question", "text": "...", "chars": 55}
      ],
      "description": "..."
    }
  ]
}
```

Follow this schema STRICTLY. No additional fields. `chars` is the actual character count of the text.
"""

    return prompt + json_instruction

def main():
    p = argparse.ArgumentParser(description="Generate Meta Ad copy via Gemini")
    p.add_argument("--brand", required=True)
    p.add_argument("--product", required=True)
    p.add_argument("--tone", required=True)
    p.add_argument("--audience", required=True)
    p.add_argument("--cta", default="Get started")
    p.add_argument("--language", default="English (UK)")
    p.add_argument("--angles", type=int, default=5)
    p.add_argument("--output", default="copy_output.md")
    p.add_argument("--model", default="gemini-2.5-flash")
    p.add_argument("--brand-voice", default=None,
                   help="Path to brand voice specification markdown file")
    p.add_argument("--format", choices=["markdown", "json"], default="markdown",
                   help="Output format: markdown (human-readable) or json (machine-readable)")
    args = p.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY not found. Set it in env or ~/.env", file=sys.stderr)
        sys.exit(1)

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(args.model)

    prompt = build_prompt(args)
    print(f"Generating copy with {args.model}...")
    print(f"Brand: {args.brand} | Angles: {args.angles}")

    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            temperature=0.75,
            max_output_tokens=16000,
        )
    )

    # Check for safety filter blocks
    if not response.candidates:
        print("ERROR: Gemini returned no candidates. Prompt may have been blocked by safety filters.", file=sys.stderr)
        print("Try adjusting --audience or --product text to avoid triggering content filters.", file=sys.stderr)
        sys.exit(1)

    candidate = response.candidates[0]
    if candidate.finish_reason and candidate.finish_reason.name == "SAFETY":
        print("ERROR: Response blocked by Gemini safety filter.", file=sys.stderr)
        print(f"Safety ratings: {candidate.safety_ratings}", file=sys.stderr)
        sys.exit(1)

    if candidate.finish_reason and candidate.finish_reason.name == "MAX_TOKENS":
        print("WARNING: Output was truncated (hit token limit). Later angles may be incomplete.", file=sys.stderr)
        print("Consider reducing --angles or running in multiple passes.", file=sys.stderr)

    try:
        output = response.text
    except ValueError as e:
        print(f"ERROR: Could not extract text from response: {e}", file=sys.stderr)
        print("This usually means the response was blocked or empty.", file=sys.stderr)
        sys.exit(1)

    if len(output.strip()) < 100:
        print(f"WARNING: Output suspiciously short ({len(output)} chars). Check quality.", file=sys.stderr)

    if args.format == "json":
        # Strip markdown code fences if Gemini wraps in ```json...```
        cleaned = output.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned.split("\n", 1)[1]  # remove first line
            if cleaned.endswith("```"):
                cleaned = cleaned[:-3].strip()

        try:
            parsed = json.loads(cleaned)
        except json.JSONDecodeError as e:
            print(f"ERROR: Gemini output is not valid JSON: {e}", file=sys.stderr)
            print("Saving raw output for debugging...", file=sys.stderr)
            fallback_path = args.output.replace(".json", "_raw.txt")
            with open(fallback_path, "w") as f:
                f.write(output)
            print(f"Raw output saved to {fallback_path}", file=sys.stderr)
            sys.exit(1)

        with open(args.output, "w") as f:
            json.dump(parsed, f, ensure_ascii=False, indent=2)

        n_angles = len(parsed.get("angles", []))
        print(f"\n✅ JSON copy saved to {args.output}")
        print(f"   {n_angles} angles, {sum(len(a.get('primary_texts', [])) for a in parsed.get('angles', []))} primary texts")
    else:
        # Existing markdown output
        with open(args.output, "w") as f:
            f.write(f"# Meta Ad Copy — {args.brand}\n\n")
            f.write(f"_Generated via {args.model} | Temperature: 0.75 | {len(output)} chars_\n\n")
            f.write(output)

        print(f"\n✅ Copy saved to {args.output}")
        print(f"   {len(output)} characters, ~{len(output.split())} words")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}", file=sys.stderr)
        print("\nCommon fixes:", file=sys.stderr)
        print("  - GEMINI_API_KEY expired? Regenerate at https://aistudio.google.com/apikey", file=sys.stderr)
        print("  - Rate limited? Wait 60 seconds and retry", file=sys.stderr)
        print("  - Network issue? Check internet connection", file=sys.stderr)
        sys.exit(1)
