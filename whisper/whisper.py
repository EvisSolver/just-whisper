
from config import *
from pystyle import Colors, Write

# --- MODEL TRANSCRIBER ---
segments, info = model.transcribe("test.mp3", beam_size = 10) # -- >10 - A lot VRAM | <10 - Not a lot VRAM
print(f"Language from .mp3: {info.language} | proba: {info.language_probability:.2f}")

def audio_callback(indata, frames, time, status):
    if status: print(status)
    audio_queue.put(indata.copy()).flatten()


for segment in segments:
    Write.Print(f"{segment.text}", Colors.purple)