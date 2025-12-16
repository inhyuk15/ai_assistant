from transformers import pipeline
import torch
import time

if torch.backends.mps.is_available():
    device="mps"
else:
    device="cpu"

start = time.time()

print("Loading Whisper model...")
whisper = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-base",
    device=device
)

load_time = time.time() - start

audio_file = "slurp_test.wav"
print(f"\nTranscribing: {audio_file}")

start = time.time()
result = whisper(audio_file)

inference_time = time.time() - start

print("\n" + "="*50)
print("TRANSCRIPTION:")
print(result["text"])
print("="*50)

print(f"loading mode: {load_time}, \n\n inference_time: {inference_time}")