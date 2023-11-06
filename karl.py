import whisper

model = whisper.load_model("base")
result = model.transcribe("/content/test.mp3")
print(f' The text in video: \n {result["text"]}')