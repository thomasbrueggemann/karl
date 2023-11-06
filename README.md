# 🤖 Karl

Karl will be the brain of a little robot friend. The inspiration came from watching the following YouTube video. While the hardware in the video is pretty retro-awesome, I think it would be a smart move to leave any Alexa/Siri/... assistants behind as the core brain, but instead leverage some of the recent AI models to power Karls brain.

[![The coolest robot I've ever built!](https://github.com/thomasbrueggemann/karl/assets/2313087/9fbb5b1a-f0ff-4594-919c-e545fbe480e1)]([https://youtu.be/StTqXEQ2l-Y?t=35s](https://www.youtube.com/watch?v=bO-DWWFolPw) "The coolest robot I've ever built!")

## Karls Birthjournal

### Step 1: Whisper

The first step will be to implement speech-to-text capability for Karl. For that we run a high-bandwidth speech recognition model called "Whisper", open-sourced by OpenAI, locally.

https://medium.com/@kharatmoljagdish/using-openai-whisper-python-library-for-speech-to-text-dda4f558fccc

### Step 2: Dream

There seems to be a high-bandwidth alternative to ChatGPT, called https://gpt4all.io/index.html We'll look into that, if that can be fed the transscibed text from Whisper to process the response.


_to be continued..._
