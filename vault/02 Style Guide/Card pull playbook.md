---
tags: [style, card-pull, template]
---
# Card pull playbook (Backyard Breaks stream clips)

Back to [[START HERE]] · From: [[Card pull and clip refs D-G]] · Code: `src/CardPull.tsx` + plan `src/flagg.ts`

Footage from the stream sheet is already vertical: **hosts cam on top (y 0–420), a burned-in white banner (y ~427–607), card cam below.** We cover the burned banner with our own.

## Structure (≈25–30 s)
1. **Hook (0–1.5 s):** open on the loudest reaction (hosts jumping/screaming) with our banner already up. Whip into the start.
2. **Rips (fast):** only the "come on, come on" + named hits (2–4 s each), every cut a motion-blur whip + whoosh. Name captions when a player is said.
3. **Reveal:** whip + punch-in on the card, red arrow jabs at it, vine boom, title stacks in: **PLAYER** (white) / **PARALLEL 1/1** (red) / **$PRICE** (green, cha-ching).
4. **Reaction layout:** hosts cam enlarged on top (red circle **tracking** whoever is losing it), our banner under it, big card still + title below. Air horn + crowd under the real screams.
5. **End:** engagement question ("WOULD YOU KEEP IT OR SELL IT? 🤔") with a ding.

## Text
- Banner: white box, black Montserrat 800, keyword colors red (rarity) / green (money), from the sheet's value + card name.
- Captions: our glow style ([[Caption style]]) centered mid-frame, + iOS emoji. `*ASTERISK*` captions for screams/jumps.

## Sheet → edit
Sheet: `1eX0vqF73N9x2gtkRbalnKMHRd3nbd-CEv0Rt4D2glM4` ("Backyard Breaks — Clip Context Tracker"). Export a tab: `https://docs.google.com/spreadsheets/d/<ID>/export?format=csv&gid=<GID>`. Checked 2026-11-14.

| gid | Tab | Rows | Use |
|---|---|---|---|
| 1203111212 | 🏆 Historical Big Pulls | ~58 | **Clip 1st.** All-time biggest $ pulls. |
| 183567664 | 📈 Historical Viral Content | ~22 | Published hits + views. Copy the format, not the clip. |
| 133317179 | Recent most viral moments (stream pulls) | **902**, 2026-03-09 → 2026-11-09 | Big pile. Pick by value + hype. |
| 1029565171 | Trevor stream (talk clips) | 19 | All edited already. |
| 1123252542 | How to use | — | Rules below. |

**Columns** (pull tabs): Drive Link · Approximate Date · Card Name / Description · Card Value (USD) ⭐ · *PSA 10 Card Value (recent tab only)* · Product/Collection · Why It Was Special · Suggested Caption / On-Screen Text · Hype Level · Notes for Clippers.

**Rules from the How-to tab:**
- **Priority:** Big Pulls → Viral Content → stream clips.
- **Card value always on screen** (banner `$PRICE`). Range ok ("$500–$1K"). PSA 10 value only to raise it, when filled.
- **Suggested Caption = hook text.** Use it or close. Biggest lever.
- **Hype:** 🔥 INSANE $5K+ · ⚡ HIGH $1–5K · 📈 MEDIUM $200–1K · 💤 LOW skip.
- Drive link private → skip row.
- Read "Notes for Clippers" before cutting.

**Jorho rules still apply:** captions always on, top line not about Trevor, Jorho intro + "TREVOR LAWRENCE · NFL QB" label, blur/beep unrevealed cards, open with a hooks-folder scream hook, 15–25 s (trim the structure above to fit).

## Suspense → reveal recipe (user: "no suspense", "reveal isn't shocking", v3)
**Build (~3.5 s before the reveal):**
- The card is **blurred with ❓** the whole time, and the hook/banner never name the player.
- Last ~1 s of source before the reveal plays in **slow motion (0.4×)**, dialogue muted.
- Card cam **creeps in** (up to 1.35×), **desaturates**, and **trembles harder** each frame; a **vignette closes in**.
- **Heartbeat** from the start of the build, a **riser** whose peak lands on the reveal, music intro building **louder**, then **250 ms of silence** before the drop.
- "**WAIT FOR IT... ⏳**" blinks for the last second. Narrator whispers "Then... the next card came out."

**Reveal (one frame, everything at once):**
- **White flash** (2 frames) → **green flash**, a **big screen shake** (16 frames), and a **zoom slam** (2.2× snapping back to 1.5×).
- A giant red **"1 OF 1" stamp** slams on (scale 3.2 → 1), with the title stack, an arrow on the printed 1/1, and **falling money**.
- Sound: the **music drop**, a bass-boosted vine boom, an 808 boom, ka-ching, then the hosts screaming.

## AI narration
- ElevenLabs (this connector). **User: "only use Alex voice"** → voice **"Alex - Young American Male"** (`yl2ZDV1MzN4HbQJbMihG`, saved in the user's own ElevenLabs workspace). Never use another voice, model `eleven_v4`, tags `[confident]`, `[intrigued]`, `[whispering]`, `[excited]`, `[playful]`.
- Generate **all lines in one take** with `[long pause]` between them, then place each line by its file range (find the ranges with `scripts/speech_segments.py file -40`, word times with `scripts/transcribe_words.py`).
- **Loudness (user: "voice can't be heard"):** run the narration through `acompressor=threshold=-30dB:ratio=6:makeup=10dB,loudnorm=I=-11:TP=-1` (→ `full_loud.mp3`) so the whisper is as loud as the hype. Under the narrator: hosts at **18 %**, music at **0.06–0.09**, and hype SFX (air horn, crowd) kept low.
- Narrator explains the moment, the hosts' mic is ducked under it, and the narration gets the captions (in chunks of 3 words). Keep the hosts' own captions only where the narrator is quiet.
- Line pattern: setup ("…hunting for one card") → near misses ("big names… but not the one") → whispered tease before the reveal → hype reveal (player, parallel, 1/1, price) → question at the end.
- ⚠️ 2026-10-24: ElevenLabs disabled the user's **free tier** ("unusual activity… proxy/VPN"). One take succeeded and the second failed. **Fix that works:** make one generation call at a time, a few minutes apart (never parallel). That covered all 6 batch-1 narrations.
