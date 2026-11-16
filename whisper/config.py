import queue
from faster_whisper import WhisperModel

# --- MODEL ---
model_size = "large-v3" # -- 'small' the smallest model, 'large-v3' the biggest model
model = WhisperModel(model_size, device = "cuda", compute_type = "float32") # -- Model setting's

# --- AUDIO ---
audio_queue = queue.Queue()
audio_buffer = []

# --- MODEL PARAMETERS ---
samplerate = 16000

block_duration = 0.5
chunk_duration = 2

channels = 1

frames_per_block = samplerate * block_duration
frames_per_chunk = samplerate * chunk_duration


dtype = "float32"