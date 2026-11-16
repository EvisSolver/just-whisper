import threading
import numpy as np
import sounddevice as sd

from config import *
from pystyle import Colors, Write

# --- MODEL TRANSCRIBER ---
segments, info = model.transcribe("test.mp3", beam_size = 10) # -- >10 - A lot VRAM | <10 - Not a lot VRAM
print(f"Language from .mp3: {info.language} | proba: {info.language_probability:.2f}")

# --- AUDIO-CALLBACK ---
def audio_callback(indata, frames, time, status): # -- Putting indata.copy in audio_queue
    if status: print(status)
    audio_queue.put(indata.copy())

def recorder(): # -- Record audio each 200ms
    with sd.InputStream(samplerate = samplerate, channels = channels, callback = audio_callback, blocksize = frames_per_block):
        Write.Print("|", Colors.green, interval = 0)
        while True: sd.sleep(200)
def transcriber(): # -- Writting Transcribed text
    global audio_buffer
    while True:
        block = audio_queue.get()
        audio_buffer.append(block)

        total_frames = sum(len(b) for b in audio_buffer)
        if total_frames >= frames_per_chunk:
            audio_data = np.concatenate(audio_buffer)[:frames_per_chunk]
            audio_buffer = [] # -- Clearing buffer

            audio_data = audio_data.flatten().astype(np.float32)

            segments, _ = model.transcribe(audio_data, language = language, beam_size = beam_size, vad_filter = True)
            for segment in segments:
                Write.Print(f"{segment.text}", Colors.purple)

threading.Thread(target = recorder, daemon = True).start() # -- Starting Thread with daemon
transcriber()