import numpy as np
import sounddevice as sd

from config import *
from pystyle import Colors, Write

# --- MODEL TRANSCRIBER ---
segments, info = model.transcribe("test.mp3", beam_size = 10) # -- >10 - A lot VRAM | <10 - Not a lot VRAM
print(f"Language from .mp3: {info.language} | proba: {info.language_probability:.2f}")

def audio_callback(indata, frames, time, status):
    if status: print(status)
    audio_queue.put(indata.copy())

def recorder():
    with sd.InputStream(samplerate = samplerate, channels = channels, callback = audio_callback, blocksize = frames_per_block): Write.Print("|", Colors.green, interval = 0)
    while True: sd.sleep(200)
def transcriber():
    stream = sd.InputStream(samplerate = samplerate, channels = channels, dtype = dtype)
    stream.start()
    buffer = np.array([], dtype = np.float32)

for segment in segments:
    Write.Print(f"{segment.text}", Colors.purple)