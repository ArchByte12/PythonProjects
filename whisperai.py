import sys
import whisper
import os

# Check if the user gave an audio file as input
if len(sys.argv) < 2:
    print("Usage: python whisperai.py <audiofile>")
    print("Or drag & drop an audio file onto whisperai.py")
    sys.exit(1)

# Get the audio file path from arguments
audio_file = sys.argv[1]

# Check if the file exists
if not os.path.exists(audio_file):
    print(f"File not found: {audio_file}")
    sys.exit(1)

# 🔹 Load a more accurate model (small or medium are good for CPU)
print("Loading Whisper model... (this may take a bit)")
model = whisper.load_model("medium")

# 🔹 Transcribe with accuracy tweaks
print("Transcribing... please wait")
result = model.transcribe(
    audio_file,
    beam_size=5,         # better decoding
    best_of=5,           # choose best among candidates
    temperature=0.2,     # stable output
    fp16=False           # force CPU-friendly mode
)

# Print transcription with timestamps
for segment in result["segments"]:
    start = segment["start"]
    end = segment["end"]
    text = segment["text"]
    print(f"[{start:.2f} --> {end:.2f}] {text}")

# Save output to text file
output_file = os.path.splitext(audio_file)[0] + "_transcription.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for segment in result["segments"]:
        start = segment["start"]
        end = segment["end"]
        text = segment["text"]
        f.write(f"[{start:.2f} --> {end:.2f}] {text}\n")

print(f"\n Transcription saved as: {output_file}")
