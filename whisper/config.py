import queue
from faster_whisper import WhisperModel

# --- MODEL ---
model_size = "large-v3" # -- 'small' the smallest model, 'large-v3' the biggest model
model = WhisperModel(model_size, device = "cuda", compute_type = "float16") # -- Model setting's
audio_queue = queue.Queue()

# --- MODEL PARAMETERS ---
samplerate = 16000
channels = 1
dtype = "float16"