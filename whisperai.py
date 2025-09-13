import whisper

# Load the model (base is a good start: small + fast + accurate)
model = whisper.load_model("base")

# Transcribe your audio file
result = model.transcribe("recording.mp3")

# Print the text
print(result["text"])
