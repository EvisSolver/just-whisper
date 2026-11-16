from config import *

# --- MODEL TRANSCRIBER ---
segments, info = model.transcribe("test.mp3", beam_size = 10) # -- >10 - A lot VRAM | <10 - Not a lot VRAM

print(f"Language from .mp3: {info.language} | proba: {info.language_probability:.2f}")