# Figma / FigJam build

Board URL `figma.com/board/:fileKey/...?node-id=a-b` -> fileKey, nodeId `a:b`. Call `create_session` first (fileKey, description), then `use_figma` with `skillNames` "resource:figma-use,resource:figma-use-figjam" (read the skills as MCP resources `skill://figma/figma-use/SKILL.md` and `skill://figma/figma-use-figjam/SKILL.md` if they are not installed). Read with `get_figjam` (not `get_metadata`) and `get_screenshot` with a nodeId; download the screenshot with curl and view it.

## Pitfalls
- Every call: select the page with `figma.setCurrentPageAsync(page)` (at most once per call). FigJam has no `createPage`; clarify pages in the file beforehand.
- Load fonts before any text change: load `shape.text.fontName` of a dummy shape, `Inter Medium`, optionally `Inter Bold`. Bold first word: `text.setRangeFontName(0,n,{family:'Inter',style:'Bold'})` in try/catch.
- **FigJam repositions new sections by itself** (it places them next to existing ones). Set `sec.x`/`sec.y` again at the end of the script and verify with a read-only call.
- Text blocks in shapes: estimate height, `cpl=floor((w-48)/(fs*0.52))`, lines times 1.12 plus 1, otherwise text gets cut. After building, check a screenshot; if text is cut, add one line of height and restack the columns.
- Use `text.textAlignHorizontal='LEFT'` for running text in cards.
- Tables: `createTable` is capped at 23 rows; grow with `insertRow(numRows)` up to 45 rows per table; split longer lists across tables. Column width via `resizeColumn(i,w)`, cells via `cellAt(r,c).text.characters`.
- A call must not exceed 50,000 characters of code: put data per match or per table in separate calls; generate the data with a script into a `.js` file first and paste its content.
- Failed calls roll back; still check with a read-only call before retrying.
- Always return all created IDs and heights.
- Colors passed to paint/stroke are `{r,g,b}` objects in 0..1; do not pass arrays or already converted objects through the converter twice.

## Colors (0-255, divide by 255 in code)
- Top effect: fill 255,205,194, stroke 255,117,86 · direct effect: 255,224,194 / 255,158,66 · core problem: 255,117,86 / 220,48,9, white text · cause: 61,173,255 / 0,122,210, white text · sub-cause: 194,229,255 / 61,173,255 · section: 249,249,249 · text 30,30,30 · stroke weight 4.
- Status cards: active 194,229,255/61,173,255 · acquired 232,232,232/150,150,150 · shut down 255,205,194/220,48,9 · unverified 255,243,194/255,196,0. Home-market HQ: red border 237,41,57, weight 8, a small red sticker (64x40, white text) with the country code; "active in the home market, HQ elsewhere": white sticker with red border.
- Funding tiers: >= 100M 27,94,32 (white text) · 20-100M: 67,160,71 (white) · 5-20M: 165,214,167 · 1-5M: 220,237,200 · < 1M: 255,236,179 · bootstrapped 225,245,254 · amount not stated 224,224,224 · nothing found 250,250,250 (grey text).

## Problem tree layout (section 2768 wide)
Title text 56 pt at (64,48). Top effects y=200 (x=228+896i, 520x96) · direct effects y=436 (400x102, centered, pitch 448) · core y=678 (x=784, 1200x96) · causes y=914 (400x102, centered, pitch 448) · sub-causes below from y=1064, x=cause+32, 336 wide, height 102/121/145 by text length, gap 24. Connectors: `figma.createConnector()`, ELBOWED, `connectorEndStrokeCap='ARROW_LINES'`, weight 4, start `{endpointNodeId,magnet:'TOP'}`, end `{magnet:'BOTTOM'}`; direct effect -> top effect and core -> direct effect in red (255,117,86), cause -> core in blue.

## Match board
One row per match: demand card left (orange) -> middle (red, "Match n (strong/chain/...)") <- supply card right (blue, lines "Tree k (category): ..." with source). Connectors RIGHT->LEFT and LEFT->RIGHT. Below: "Weaker matches", "No counterpart", "Notes" (neutral, source quality only). To add a match later, shift everything below the last row down and insert the new row.

## Startup sections per match
7 columns (home market, Europe without home market, North America, South America, Asia, Africa, Oceania), card 440 wide, gap 28. Header: description + "Findings in the home market according to research" + legend. Card: name (bold), country · type · status · coverage, description, "Fit", "Traction" (cut at sentence boundaries, URLs reduced to the domain), domain. Funding box on the card edge (card y minus 20), funding legend top right. Sections side by side in one row, one section per match.

## Problem-and-cluster sections
Title, red core field "Common problem (both sides)", two fields below (anchor view orange, partner view blue), heading "Startups by solution approach", then per cluster: a blue header box (name and count), a grey box "Approach: ... / In home market: ...", below it chips 360 wide (name bold, country · status, funding). Order within a cluster: home-market HQ first, then other home-market countries, then the rest. Place the row above the match board (negative y), sections side by side.

## Table
Columns: #, venture, HQ, match, funding according to source, approx. amount, last round, investors, acquisition, source, reliability | note. Blue header row, amount cell colored by tier. State the exchange rates and the source-level definitions above the table. Second table for "funding known but amount missing / undisclosed / bootstrapped"; below it a name list "No funding found (n)".
