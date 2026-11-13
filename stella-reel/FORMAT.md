# The format, measured

Every number here comes from 32 distinct talking-head edits of @stella.soragi (Sept-Oct 2026), analyzed frame by
frame: Apple Vision OCR + face landmarks at 5 fps, frame-difference cut detection with background-scale checks,
mlx-whisper word timestamps, Demucs voice/effects separation, CLAP labels on every sound event. Ranges are p10-p90
across the 32 edits unless stated. Pixel values are for the 1080x1920 delivery; double them for a 2160x3840 master.
Look at [assets/style-board.jpg](assets/style-board.jpg) (24 labeled frames) next to this file.

## Delivery

| | |
|---|---|
| Canvas | 1080x1920, 30 fps (master at 2160x3840 is fine: scale every px value x2) |
| Duration | median 75 s (63-89 s; shortest 55 s, longest 131 s) |
| Words | median 237 (209-294) |
| Speech rate | median 198 wpm (185-224); stories run slower (164), tutorials faster (225-238) |
| Loudness | delivered files measure -14.8 LUFS in every edit (platform-normalized; their true peak goes above 0 dBTP). Master at -14 LUFS integrated, true peak <= -1 dBTP |
| Music | none, in 32 of 32 edits (effects stem floor -66 dB = silence) |

## Camera and set

- iPhone **front camera** on a fixed stand at eye level, on a dining table. Static: background drift p90 0.6 px
  between frames. Same spot every day, so the room becomes part of the brand.
- **Medium close-up**: face height = 21.7% of frame height (20-24%), eye line at 40.5% from the top (37-43%),
  top of the forehead ~34%, hair top ~26-28%. Table edge visible at the bottom, chest and hands in frame.
- **Off-center**: face center at 36-44% of the width in the October originals (42-62% in the September episodes);
  the opposite side is the free side for overlays. Her re-posts flip the frame, so which side doesn't matter: keep
  one side free.
- She **holds the wireless lav mic** (black furry windscreen) at chest height in one hand the whole time; the other
  hand gestures (counting on fingers for numbered lists, pointing, waving). The mic is part of the look.
- **Light**: daylight from big windows (trees outside) behind/beside her; white ceiling with a square recessed light
  in the top band, which is where the text sits (bright, low-detail background for white text).
- **Wardrobe**: everyday clothes, different each video (shirt, cardigan, hoodie), hair down with bangs. No set
  dressing beyond the real room (kids' toys sometimes visible).
- **Delivery**: looks at the lens, speaks fast and warm, small smiles at punchlines, voices other people (changes
  tone) when quoting them.

## Opening (frame 0)

All 32 edits start in motion: her hand sweeping away from the lens (the tap that started the recording), kept in the
edit. On frame 0 at the same time: she is already speaking (first word at 0.00 s in 32/32), the hook text is already
on screen, and a low boom hits (28/32 at -7..-19 dB peak, median -10.5 dB, louder than the voice; 3 softer, 1
without). Her boom is in [assets/sfx](assets/sfx): put it at frame 0 and its peak lands ~0.32 s in. Nothing precedes
the hook: no intro, no logo, no greeting.

## Cutting

- **Jump cuts only.** No transitions, no B-roll cutaways (exceptions: full-screen screen recordings in tutorials,
  a 1-2 s gag clip).
- **One sentence = one shot.** 82% of sentences start on a cut; 71% of cuts land on a sentence start. The other
  cuts remove a stumble mid-sentence or set up a punch-in on the key phrase.
- 20 cuts per minute (14-25); average shot 2.9 s (2.3-4.0 s).
- **Pauses removed**: gap between words p90 = 0.08 s; at most 1-2 pauses over 0.3 s per video; breaths cut.
  Natural sentence rhythm survives only inside a sentence.

## Punch-ins

- 23% of shots (9-40%) are a **digital punch-in**: the same take scaled **1.18x** (1.12-1.25, max 1.5),
  centered on the face (horizontal shift 0), eye line ~1% higher. Static scale: no animated zoom inside a shot.
- Mostly isolated between base shots (72% of punch-ins return to base on the next cut). Median punch-in shot 2.7 s.
- Cuts and punch-ins carry no sound of their own (an SFX lands on a cut only when text appears there).
- Where: see [EDIT-RULES.md](EDIT-RULES.md#shots).

## Text styles

Five core styles plus three rare ones. All white, sentence case, centered, no outline, no box, no visible shadow
(measured darkening around the glyphs <= 2%: the heavy weight on the bright ceiling band carries legibility).
Closest free fonts are in [assets/fonts](assets/fonts) (OFL); in the Edits app pick the built-in font that matches
the style board.

| Style | Look | Size @1080 | Where | Motion |
|---|---|---|---|---|
| **Hook serif** | high-contrast display serif, white (closest: Instrument Serif, a touch heavier) | ~100 px, line pitch ~100 px (leading 1.0), 1-3 lines, max width ~720 px | block top y = 250 px (13%), bottom ~530 px (28%) | on at frame 0, off on the cut after the hook sentence(s), 3-8 s in |
| **Handwritten add-on** | thin handwriting, slightly slanted (closest: Gochi Hand) | ~50 px | right under the serif block | typewriter, starts on its spoken words |
| **Headline** | heavy italic geometric sans (closest: Poppins ExtraBold Italic) | ~80 px (line pitch ~85 px); one-word punch ~150-190 px | text top y ~ 250-330 px (13-17%), bottom <= 610 px (32%); lists may reach 750 px (39%) | hard in on the spoken word, hard out on the next cut/topic |
| **Typewriter subtitle** | same italic sans, smaller (the hook serif in the "Como eu posto…" series) | ~50 px, line pitch ~68 px, 2-4 lines | under a headline label (series card) | typewriter + typing SFX |
| **Caption word** | the hook serif, small, lowercase as spoken, with punctuation | ~55 px | beside the face at mouth/chin height: x 27-67% (on the free side or by the mic), y 52-63% | one word at a time, synced to speech, whole video (30/32) |
| Label box | black italic sans on a white rectangle | ~45-55 px | top band | hard in |
| Data mono | typewriter monospace caps ("30 VÍDEOS") | ~45 px | top band | typewriter |
| Display caps | heavy rounded caps, sometimes rotated ("YAP", "MEGAZORD", "Tenta ENSINAR") | ~150-200 px | top band | hard in, rare (1 per video at most) |

Variations of the hook serif: the number on its own bigger line ("R$ 51.000"); the key word as BIG serif caps
("DINHEIRO", swapped to "RECONHECIMENTO" when spoken); a reflective line tinted cream `#F9F5BC`
("Mas ela existe…"); an emoji replacing a word inside the line ("Um deles com uma 🐝"); a small italic kicker above
it ("Episódio 4", "Nos últimos 32 dias..").

Colors: text `#FCFCF9`; annotation red `#F45B3D` (hand-drawn ellipses, underlines, arrows); cream `#F9F5BC`;
label box white with black text; emoji in native color.

## Layout zones (y as % of frame height)

```
  0- 4%  Instagram header area — nothing
  4-13%  top band: wide screenshots, comment cards, memes, emoji rows (when a headline is also on, they sit above it)
 13-32%  TEXT ZONE: hook block, headlines, lists, series card (over the ceiling/window, above the hair)
 26-34%  hair / forehead: headline bottom may touch it; a screenshot at the top pushes the headline down to here
 34-50%  face: eyes ~40% — never covered (except full-screen inserts)
 25-65%  free side (x 55-95% or 5-45%): vertical cards, thumbnails, cut-out photos, product images
 52-63%  caption word, beside the chin
 55-80%  chest band: profile headers, payout cards, comment clouds, tool cards
 80-100% Instagram caption/UI area — nothing important
```

## Overlays

All overlays are hard in on the spoken word and hard out on the next cut or topic change. No borders, no rounded
frames added, no drop shadows, no entry animation.

| Overlay | Look | Size / place |
|---|---|---|
| Proof screenshot | the real screenshot (Insights, sales dashboard, statement, payout card), cropped tight to the number, light UI kept as is | 45-75% width; top band or chest band |
| Red annotation | hand-drawn ellipse / underline / arrow in `#F45B3D`, added on the exact number or word when spoken | over the screenshot |
| Profile header | her profile header (avatar, posts, followers, following), follower count circled or arrowed | ~50% width, chest band or top band |
| DM / comment cards | real messages, one or a cascade of many (social proof), key phrase underlined | 50-85% width; cascades fill the left/center for 1-2 s |
| Referenced video | the reel she talks about, as a playing vertical card | ~28% width, free side by the face |
| Cut-out photo | PNG cut-out of a person she names, sometimes with a 💬 bubble | ~20% width each, top band, one per name as spoken |
| Meme / film still | small landscape card for a joke or dramatic beat | ~50% width, above the head |
| Emoji sticker | native emoji: a row built one per spoken noun, an equation (👩‍💻 + 📄 = 📒), or one big sticker (😳) | rows ~80-100 px each; big ~200 px |
| Mock UI | Instagram-style toggle, app pill (icon + name in a colored rounded pill), "follow" pill with avatar, pointer cursor | 35-60% width |
| Screen recording | full-screen phone recording for click-by-click steps, red arrows on each button | full frame, 1-2 s per step, voice continues |
| Giant quote marks | “ top-left and ” bottom-right framing her face while she reads someone's words | ~150 px glyphs |

## Animation

- **Hard in, hard out** for everything: text, screenshots, emoji, stickers. No fades, slides, bounces or scale-ins.
- **Typewriter** is the only text animation: ~1 character per frame (25-30 chars/s), used for the handwritten
  add-on, the series subtitle, voiced quotes and long sentences. It always has the typing burst, running for the
  whole reveal (see Sound). The Edits typewriter runs ~20 chars/s, so there a reveal lasts characters ÷ 20 s.
- **Builds**: emoji rows, and lists she keeps referring to (steps, a ❌ checklist), grow item by item on each spoken
  item and stay until the topic ends; items that each get their own explanation replace one another instead.
- **Swaps**: a headline is replaced instantly, usually on the next cut (headline state changes every ~1 s: median
  1.0 s, p90 2.4 s, because lists keep growing).
- Text appears on the spoken keyword: median +0.06 s after the word starts.

## Coverage and density

| | median | p10-p90 |
|---|---|---|
| Time with headline text on screen | 66% | 41-83% |
| Headline changes per minute | 27 | 20-44 |
| Text-free stretch | 1.8 s | up to 5.4 s (max 20 s, in stories/confessions) |
| Series tag on screen | 18 of 32 edits | at 5-15 s (median 9.9 s) |

## Sound

Voice only, close lav mic, dry room. No music bed. Sound effects follow graphics: 65% of new text blocks get one;
cuts and punch-ins without new text almost never do (20%, mostly coincidental). Audible SFX: median 23 per minute
(11-34), about one every 2.6 s while text is changing; none during clean stretches.

Her six core sounds are identified exactly: each was matched (normalized cross-correlation) against her effects
stems. Three are in the Edits sound library; the other three are rebuilt as the per-sample median of every
occurrence in her stems. All six are in [assets/sfx](assets/sfx). Use these, never look-alikes (stock
substitutes sound wrong), and the worst miss is a single keystroke where she plays a typing burst.

| Sound | Source | Hit in the file | Level vs voice | Used for |
|---|---|---|---|---|
| **Low boom** | rebuilt, median of 78 occurrences: ~73 Hz body with drum-skin partials at 125-480 Hz (a sub-only boom is silent on a phone speaker) | slow attack, peak ~0.32 s after the element start, as in her edits | **+1.9 dB** | frame 0 (28 of 32 edits); a big number reveal; a negative punchline ("Strike"); the biggest overlay entrances |
| **Soft click** | Edits library "Clique de mouse (único) 2" (`1295791565463305`): a press and a release 90 ms apart | press ~5 ms after the element start | **-12.4 dB** | most new headlines and overlays; every image or screen entering |
| **Typing** | Edits library "Digitando (rápido) 1" (`580187595083522`): a continuous burst of ~9-10 keystrokes/s, 8.4 s long | first key ~10 ms after the element start | **-8.1 dB** | every typewriter reveal, from its first character to its last |
| **Tick** | Edits library "Clique de mouse (único) 1" (`801813285845459`): a soft hit, then the main one 90 ms later | first hit ~5 ms after the element start | **-8.8 dB** | each emoji of a row, each list item or card of a cascade, each screen-recording step |
| **Ding** | rebuilt, median of 50: a typewriter bell, partials ~2.8 and 6.2 kHz, ~0.8 s ring | onset ~30 ms after the element start | **-11.7 dB** | money and result lines, ~0.35 s after the click of the text it rings on |
| **Low thud** | rebuilt, median of 52: a low "tock" with partials ~2.6 and 3.6 kHz | onset ~15 ms after the element start | **-1.5 to -2 dB** | ❌ items, failures ("Pix nunca pagou") |

Rare sounds, not identified. Levels here are peaks in her delivered mix, not offsets from the voice:

| Sound | Spec | Peak in her mix | Used for | Reference |
|---|---|---|---|---|
| Vine boom | 1-3 s sub drop | -14 dB | the strongest negative or ironic beat, once per video at most | — |
| Blip / drop | 0.08 s, ~700 Hz | -16..-27 dB | a toggle flipping, a small sticker | `blip__*.wav` |
| Literal foley | crickets, cash register, coins, record scratch, sparkle | -16..-37 dB | when the screen says it ("*cri cri cri*", "R$") | `chirp__*.wav` |

**There is no swipe.** What the corpus labels "swipe" is not one sound. Some are her boom; others are her click with
a short bright swish ~0.2 s later; one is a burst that ends in her ding. When an image or screen enters, play the
click. Play the boom only for the biggest entrances.

**Levels.** "Level vs voice" is the SFX's loudest 10 ms RMS window minus the voice's p95 10 ms RMS frame, both on
(L+R)/2 (median across her corpus). `ffmpeg -ac 1` reads about 3 dB hot on stereo, so don't measure with it.
Measure the voice on the edited cut: the raw take reads low because of its pauses and retakes (IMG_2938: -19.1 dB
raw vs -16.3 dB edited).

**Files.** Each file in [assets/sfx](assets/sfx) is cut so its hit sits a few ms after the start, so the element
starts on the graphic's frame. The files are leveled for a voice p95 of -16.3 dB.
[scripts/level_sfx.py](scripts/level_sfx.py) writes copies leveled for another video's voice, which then play at
volume 1.0.

The click, tick and typing come from the Edits library, so they are fine to publish from Edits. The boom, thud and
ding are rebuilt from her published reels. The clips in
[assets/sfx-ref](assets/sfx-ref) are cut from her effects stem at their original level (file name: source reel,
time, peak dB). They are for comparison only, not for the edit.

## Color

No stylized grade: iPhone processing in window daylight. Mean luma 118/255 (105-127); saturation moderate (62/255,
52-75); white balance warm (R/G 1.11, 1.07-1.22; B/G 0.94); blacks slightly lifted (p1 ≈ 8.5); whites ~241, nothing
clipped; soft contrast (luma std ~60). Day-to-day variation comes from weather and time of day (cloudy = darker and
warmer; one evening edit at luma 85). Match it by shooting in daylight facing a window and leaving the grade off.
