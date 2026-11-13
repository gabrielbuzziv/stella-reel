---
name: stella-reel
description: Stella-format reels — Stella Soragi's Yap talking-head diary format (PT-BR), measured from 32 of her edits. Use to write a roteiro in her format, to turn raw takes into a frame-accurate edit plan with the prints, images and SFX it needs, or to QA a finished edit against her numbers ("formato da Stella", "estilo Stella Soragi", "formato Yap").
---

# Stella-format reel

The format is a **serialized diary told to camera**: one person at a table, phone on a stand, the real story with
exact numbers, "Episódio N" of a series. In the edit, **one sentence is one shot**, the key phrase of each sentence
**lands on screen on the word** it is spoken, every claim gets its **real proof** (screenshot + red mark), a soft
click marks each new piece of text, and there is no music. Make the user's own story in this shape; never reuse her
content.

| File | Holds |
|---|---|
| [FORMAT.md](FORMAT.md) | every measured number: camera, cuts, punch-ins, text styles and sizes, layout zones, overlays, animation, SFX palette and levels, loudness, color |
| [SCRIPT.md](SCRIPT.md) | beat map, video types, hook formulas, body devices, CTAs, voice, skeleton |
| [EDIT-RULES.md](EDIT-RULES.md) | per-sentence decisions: cut or punch-in, what becomes text, which overlay, emoji, SFX, when the screen stays clean |
| [PLAN.md](PLAN.md) | deliverable formats (plan .md/.json, asset list), worked example, cutting with `reel`, execution routes, QA |
| [CORPUS.md](CORPUS.md) | the 32 reference edits, what each one teaches, where the evidence lives |
| [assets/style-board.jpg](assets/style-board.jpg) | 24 labeled frames, one per style element: look at it before writing any on-screen copy |
| [assets/sfx](assets/sfx), [scripts/level_sfx.py](scripts/level_sfx.py) | her six exact sound effects, cut on the hit, and the script that levels them for a video's voice |

## Roteiro (script)

1. **Material.** From the user: the result (numbers, dates), the story behind it, the constraint that makes it
   remarkable, the proofs they can screenshot, the deliverable or offer, the series it belongs to. Done when the hook
   has a real number or a concrete scene, and the CTA type is chosen (SCRIPT.md, Closes). Ask only for what blocks this.
2. **Shape.** Pick the video type and lay out the beat map with target seconds (SCRIPT.md). Done when every beat has
   a one-line intent and the total budget is set (≈200 words per 60 s).
3. **Write** in PT-BR, first person, conversational, exact numbers, sentences that each survive as their own shot.
   Done when: word count within the budget ±10%; hook spoken in the first sentence; series tag by ~10 s if the video
   belongs to a series; one principle line; CTA in the last 10 s; every accent and cedilla right.
4. **Annotate** each sentence for the edit with EDIT-RULES.md: text (style + exact copy) or clean, overlay, emoji,
   SFX, punch-in. Done when every sentence has a decision in every column and the coverage fits the type's target.
5. **Deliver** the script, the annotation table, the asset list (PLAN.md format) and recording notes: phone on a
   stand at eye level, front camera, window light, face ~40% from one side, lav mic in hand, start talking as the hand
   leaves the lens, one take per sentence with a clean restart on any stumble.

## Plano de edição (raw takes → plan)

1. **Cut** as in PLAN.md (Cutting the takes): last clean take of each sentence, pauses tightened to her rhythm.
   Done when the edited transcript reads complete, no retake survives, and every word has a record frame.
2. **Shots.** Cut at every sentence start; choose punch-ins (EDIT-RULES.md, Shots). Done when each shot has frames and
   a zoom (1.0 or 1.12-1.35) and about one shot in four is punched in.
3. **Layers.** Walk the transcript sentence by sentence through EDIT-RULES.md: text, overlays, emoji, SFX, all at
   word frames. Done when: hook text, boom and first word are at frame 0; every new text block has its SFX decision;
   every typewriter reveal has a typing burst as long as the reveal;
   headline coverage sits in the type's band; no text-free stretch outside stories or confessions exceeds ~5 s.
4. **Assets.** Done when every overlay in the plan has an asset row saying exactly what to capture or find and how
   to prepare it.
5. **Deliver** `stella-plan.md` + `stella-plan.json` next to the takes (PLAN.md) and name the execution route.

## QA (finished edit)

Walk the checklist in PLAN.md (QA) against the export. Done when every failed hard check is fixed or explained to the
user, each out-of-band metric is either fixed or justified by the video type, and frames of the export were compared
side by side with the style board.

## Rules that make it hers

- Frame 0 has everything at once: her voice, the hook text, the low boom, the hand leaving the lens.
- One sentence, one shot. Pauses gone (p90 gap 0.08 s). Jump cuts only; no transitions.
- Text is hard in on the spoken word and hard out on the next cut. Typewriter is the only text animation.
- White text, no outline or box, in the band above the head (13-32% of the height); eyes always visible.
- Proof is the real screenshot, cropped to the number, with a hand-drawn red mark (`#F45B3D`) on it.
- Sound follows graphics, with her exact sounds ([assets/sfx](assets/sfx)) at her levels against the voice: boom
  at frame 0, click on each new text or image, and a continuous typing burst for the whole typewriter reveal,
  never a single keystroke. No music, no SFX on plain cuts or punch-ins, no SFX in clean stretches.
- On-screen PT-BR copy is perfect: accents, cedilla, digits for numbers, her spoken words compressed.
