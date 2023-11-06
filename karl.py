#!/usr/bin/env python3

import whisper

model = whisper.load_model("tiny")
result = model.transcribe("audio.mp3")
print(result["text"])