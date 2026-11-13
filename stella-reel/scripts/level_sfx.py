"""Write Stella's SFX kit (assets/sfx) leveled for one video's voice.

Usage (from the skill directory):
  uv run -q --with numpy python -I scripts/level_sfx.py VOICE_MEDIA OUT_DIR
  uv run -q --with numpy python -I scripts/level_sfx.py --voice-db -18.2 OUT_DIR

VOICE_MEDIA is the edited talking head (cuts done, no SFX or music). Don't measure the raw take: its pauses and
retakes read low (IMG_2938: -19.1 dB raw vs -16.3 dB edited). The voice level is the p95 of 10 ms RMS frames on
(L+R)/2, the convention her levels were measured in (`ffmpeg -ac 1` reads about 3 dB hot on stereo); an SFX level
is its loudest 10 ms window. The kit is leveled for a voice p95 of -16.3 dB; every file is shifted by
(voice p95 + 16.3) dB, so each keeps her offset from the voice at element volume 1.0.
"""

import argparse
import pathlib
import subprocess
import wave

import numpy as np

SR = 48000
REFERENCE_VOICE_DB = -16.3
KIT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "sfx"


def frames_db(x: np.ndarray) -> np.ndarray:
    width = SR // 100
    count = len(x) // width
    rms = np.sqrt((x[: count * width].reshape(count, width) ** 2).mean(1))
    return 20 * np.log10(rms + 1e-9)


def peak_10ms_db(x: np.ndarray) -> float:
    width = SR // 100
    energy = np.concatenate([[0], np.cumsum(x**2)])
    return float(10 * np.log10(((energy[width:] - energy[:-width]) / width).max() + 1e-20))


def voice_p95(path: str) -> float:
    channels = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=channels", "-of", "csv=p=0", path],
        capture_output=True, text=True, check=True,
    ).stdout.strip().split(",")[0]
    raw = subprocess.run(
        ["ffmpeg", "-nostdin", "-v", "error", "-i", path, "-map", "0:a:0", "-ar", str(SR), "-f", "f32le", "-"],
        capture_output=True, check=True,
    ).stdout
    mono = np.frombuffer(raw, dtype=np.float32).astype(np.float64).reshape(-1, int(channels)).mean(1)
    return float(np.percentile(frames_db(mono), 95))


def read_wav(path: pathlib.Path) -> np.ndarray:
    with wave.open(str(path), "rb") as handle:
        frames = handle.readframes(handle.getnframes())
        return np.frombuffer(frames, dtype=np.int16).reshape(-1, handle.getnchannels()).astype(np.float64) / 32767


def write_wav(path: pathlib.Path, audio: np.ndarray) -> None:
    with wave.open(str(path), "wb") as handle:
        handle.setnchannels(audio.shape[1])
        handle.setsampwidth(2)
        handle.setframerate(SR)
        handle.writeframes((np.clip(audio, -1, 1) * 32767).astype(np.int16).tobytes())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("voice", nargs="?", help="edited talking head (any file ffmpeg reads)")
    parser.add_argument("out", help="output folder, e.g. ~/Movies/<slug>-assets for the Edits app")
    parser.add_argument("--voice-db", type=float, help="voice p95 in dB, instead of measuring a file")
    args = parser.parse_args()
    if args.voice_db is None and not args.voice:
        parser.error("pass VOICE_MEDIA or --voice-db")

    voice = args.voice_db if args.voice_db is not None else voice_p95(args.voice)
    gain_db = voice - REFERENCE_VOICE_DB
    out = pathlib.Path(args.out).expanduser()
    out.mkdir(parents=True, exist_ok=True)
    print(f"voice p95 {voice:.1f} dB -> gain {gain_db:+.1f} dB on every file")
    for source in sorted(KIT.glob("stella_*.wav")):
        audio = read_wav(source) * 10 ** (gain_db / 20)
        peak = 20 * np.log10(np.abs(audio).max() + 1e-12)
        write_wav(out / source.name, audio)
        level = peak_10ms_db(audio.mean(1))
        warning = "  CLIPS: lower the voice-relative level by hand" if peak > -0.1 else ""
        print(f"{source.name:20s} peak10ms {level:6.1f} dB ({level - voice:+5.1f} vs voice)  sample peak {peak:5.1f} dBFS{warning}")


if __name__ == "__main__":
    main()
