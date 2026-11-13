# Edit plan, assets, execution, QA

## The plan

Deliver two files next to the takes: `stella-plan.md` (for a human editing by hand) and `stella-plan.json` (same
content, machine-readable). Times are **record frames** at 30 fps from the tightened edit (frame 0 = first frame of
the reel), plus seconds for readability.

### stella-plan.md

```
# <título> — <tipo> · <duração> s · <palavras> palavras · CTA: <tipo>

| # | frames | s | fala (trecho) | plano | texto (estilo: cópia) | overlay (asset → posição) | SFX |
|---|---|---|---|---|---|---|---|
```

One row per shot; extra rows inside a shot when text, overlays or SFX change mid-shot. Every row fills every
column (write `—` for a deliberate nothing). After the table:

- **Coverage**: % of frames with headline text, longest clean stretch, number of punch-ins — against the type's
  targets in [EDIT-RULES.md](EDIT-RULES.md#density-by-video-type-her-medians).
- **Asset list** (below).
- **Open questions**: anything the takes can't answer (a number to confirm, a screenshot that doesn't exist yet).

### stella-plan.json

```json
{
  "video": "slug", "fps": 30, "width": 1080, "height": 1920, "frames": 2250,
  "type": "result breakdown", "cta": "comment keyword",
  "shots":    [{"start": 0, "end": 24, "zoom": 1.0, "note": "hook; hand leaves the lens"}],
  "text":     [{"style": "hook_serif", "lines": ["Minha aluna tinha", "1.000 seguidores", "semana passada"],
                "start": 0, "end": 119, "anim": "none"},
               {"style": "handwritten", "lines": ["e hoje tem 8.000"], "start": 77, "end": 119, "anim": "typewriter"}],
  "overlays": [{"asset": "a1", "kind": "profile_header", "start": 24, "end": 119, "box": [0.06, 0.66, 0.5, 0.12],
                "marks": [{"type": "arrow", "at": 31, "target": "follower count"}]}],
  "sfx":      [{"kind": "boom", "at": 0}, {"kind": "typing", "at": 77, "len": 9}],
  "captions": {"style": "caption_word", "x": 0.67, "y": 0.555},
  "assets":   [{"id": "a1", "kind": "screenshot", "what": "perfil da aluna com 1.128 seguidores",
                "source": "print do perfil (ou pedir à aluna)", "prep": "recortar só o cabeçalho"}]
}
```

Styles: `hook_serif`, `handwritten`, `headline`, `typewriter_sub`, `caption_word`, `label_box`, `data_mono`,
`display_caps`. Overlay kinds: `screenshot`, `profile_header`, `dm_comment`, `video_card`, `cutout`, `meme`,
`emoji_row`, `mock_ui`, `screen_recording`, `quote_marks`. SFX kinds: `boom`, `click`, `typing` (with `len`, the
reveal length in frames), `tick`, `ding`, `thud`, `vine_boom`, `blip`, `foley:<name>`; there is no `swipe` (an
image entering gets a `click`). Boxes are `[x, y, w, h]` as fractions of the frame.

## Asset list

| id | tipo | o que exatamente | de onde | preparo | usado em (frames) |
|---|---|---|---|---|---|

- Proofs come from the user's real accounts: Instagram Insights (views, followers, shares), the sales platform's
  report (Hotmart, Kiwify, Eduzz, Stripe…), bank or payout screens, DMs, comments, story replies. Capture on the phone
  in light mode; crop tight to what is spoken; blur third parties.
- Referenced videos: screen-record the reel playing (or export the user's own file).
- People: a photo per named person, background removed.
- Memes and film stills: one image per joke, landscape.
- Emoji: native, typed in the editor.
- Red marks are drawn in the editor (pen/shape tool) in `#F45B3D`, not baked into the screenshot, so they can appear
  on their word.

## Worked example (her edit, read back as a plan)

DfE52hkxxnH, first 30 s ("Minha aluna tinha 1.000 seguidores semana passada"), type result breakdown:

| # | frames | s | fala | plano | texto (estilo: cópia) | overlay | SFX |
|---|---|---|---|---|---|---|---|
| 1 | 0-23 | 0.0 | "Minha aluna tinha mil seguidores semana passada…" | 1.2x, mão saindo da lente | hook_serif: "Minha aluna tinha / 1.000 seguidores / semana passada" | — | boom @0 |
| 2 | 24-118 | 0.8 | "…e hoje tem quase 8 mil." | 1.18x | + handwritten digitado @77: "e hoje tem 8.000" | cabeçalho do perfil da aluna, faixa do peito à esquerda; seta vermelha no nº @31; o nº troca de 1.128 para 7.956 junto com "e hoje tem"; seta de novo @97 | typing @77; click @97 |
| 3 | 119-146 | 4.0 | "Tudo no remix," | base | headline: "Tudo no remix" | — | — |
| 4 | 147-174 | 4.9 | "tudo no teste." | 1.05x | headline, 2ª linha: "Tudo no teste" | — | — |
| 5 | 175-281 | 5.8 | "Até pouco tempo tinha preconceito com remix…" | punch 1.15x | headline @210: "Preconceito com remix 😬" | — | click @212 |
| 6 | 282-440 | 9.4 | "…mais de 10 mil seguidores qualificados por mês com 12 minutos por dia." | base | headline @326: "Mais de 10 mil seguidores", depois montado palavra por palavra a partir de @360: "qualificados" (grande) · "por mês" (pequeno, à direita) · "12" (grande) · "minutos por dia" (pequeno) | — | click @329; click @361 |
| 7 | 441-564 | 14.7 | "Episódio 13 de como eu tô construindo um negócio digital sendo mãe em tempo integral." | base | headline @444: "Episódio 13" + typewriter_sub @468: "Como eu tô construindo um negócio digital sendo mãe em tempo integral" | — | click @445; typing @472-517 |
| 8 | 565-680 | 18.8 | "Só que não é sair remixando qualquer coisa. Eu tenho três filtros." | 1.12x | headline @600: "❌ Remixando qualquer coisa" → @654: "3 filtros" | — | thud @600 |
| 9 | 681-754 | 22.7 | "1. O vídeo passou no meu feed e é do meu nicho." | base | headline: "1️⃣ O vídeo passou no meu feed e é do meu nicho" | — | click @687 |
| 10 | 755-820 | 25.2 | "2. Tem mais de 20 mil curtidas." | 1.04x | headline: "2️⃣ Tem mais de 20 mil curtidas" | — | click @758 |
| 11 | 821-927 | 27.4 | "3. O perfil tem mais de um milhão de seguidores e remix liberado." | base | headline: "3️⃣ O perfil tem mais de 1M seguidores e remix liberado" | — | click @825 |

Here each filter replaces the previous one because each gets its own shot; a process she will refer back to
(steps, a ❌ checklist) accumulates instead.

## Cutting the takes

Goal: the last clean take of each sentence, joined with her rhythm (p90 gap between words 0.08 s), and a word-level
transcript of the result so every word has a record frame.

- **Agent with a terminal**: transcribe the takes with word timestamps (e.g. `whisper` / `mlx-whisper` /
  `faster-whisper`, language `pt`), pick the last clean take of each sentence, keep each range from 0.04 s before
  its first word to 0.05 s after its last (0.06 s on the final word), drop pauses longer than 0.12 s, and join the
  ranges with `ffmpeg`. Transcribe the cut again to get the record frames for the plan.
- **By hand in Edits/CapCut**: split at each sentence, delete retakes and every pause; then the plan uses the times
  read off the edited timeline.

Keep the first take's hand-over-lens motion: start the first range at the first frame of the take, not at the first
word.

## Execution

- **Edits app** (what she edits in — she said she learned Edits in one week to add "esses textinhos, efeitos
  sonoros"): split the clip at each plan cut, delete the pauses, scale punch-in clips 115-130%, turn on auto captions
  with a one-word serif style, add each text layer at its frame with the font that matches the style board
  (typewriter animation only where the plan says so), add screenshots and stickers from the camera roll, add the SFX
  (below), export 1080x1920.
- **SFX in Edits:**
  1. Export the cut before adding any SFX.
  2. Level the kit for that voice: `uv run -q --with numpy python -I scripts/level_sfx.py <that export> <out folder>`
     (needs `uv` and `ffmpeg`). Without a terminal, use [assets/sfx](assets/sfx) as is: they are leveled for a
     typical close-mic voice.
  3. Import the WAVs and place each one on its plan frame at volume 100%.
  4. Trim each typing element at the end of its reveal.
  The original library names (to add them straight from Edits) are in [FORMAT.md](FORMAT.md#sound).
- **Any NLE** (Resolve, CapCut, Premiere): V1 talking head (cuts + per-clip zoom), V2 overlays, V3 text, V4 caption
  words; A1 voice, A2 SFX from `scripts/level_sfx.py` at unity gain. Fonts in [assets/fonts](assets/fonts); sizes
  and positions from [FORMAT.md](FORMAT.md) (x2 for 2160x3840). Master at -14 LUFS, true peak <= -1 dBTP.
- **Automated render**: not built; a renderer would consume `stella-plan.json`.

## QA

Check the export against her numbers in [FORMAT.md](FORMAT.md) and [EDIT-RULES.md](EDIT-RULES.md). With a terminal,
measure what you can (`ffmpeg` loudnorm for LUFS/true peak, a word-level transcript for gaps, frame grabs for
layout); otherwise watch it frame by frame.

Hard checks (fix every failure):
- Talking at frame 0, hook text on screen at frame 0, the boom at frame 0.
- No music bed.
- Running one-word captions.
- No text-free stretch over ~5 s outside stories or confessions.
- No pause left between sentences; no retake left.
- Loudness -14 LUFS, true peak <= -1 dBTP.
- PT-BR copy on screen: every accent and cedilla right.

Then compare against her bands (cuts per minute, average shot length, headline coverage, SFX per minute). Out-of-band
metrics are expected now and then (her own reels fall outside 2-4 bands each); act on the ones that cluster (cuts/min
low + avg shot high + coverage low = the edit drags). Finally put a few frames of the export next to
[assets/style-board.jpg](assets/style-board.jpg).
