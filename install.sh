#!/bin/bash

brew install ffmpeg
brew install portaudio

GPT_FILE=mistral-7b-openorca.Q4_0.gguf
if [ ! -f "$GPT_FILE" ]; then
    curl https://gpt4all.io/models/gguf/mistral-7b-openorca.Q4_0.gguf --output mistral-7b-openorca.Q4_0.gguf --progress-bar
fi

/usr/bin/pip3 install -r requirements.txt