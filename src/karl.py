
import sys

from brain import Brain
from ears import Ears
from mouth import Mouth

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 karl.py <OPENAI_API_KEY>")
        return

    openai_api_key = sys.argv[1]

    ears = Ears()
    brain = Brain(openai_api_key)
    mouth = Mouth()

    try:
        while True:
            words = ears.listen()
            response = brain.process(words)
            mouth.say(response)
            
    except KeyboardInterrupt:
        print('😴')

if __name__ == "__main__":
    main()