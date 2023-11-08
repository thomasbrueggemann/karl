
from brain import Brain
from ears import Ears
from mouth import Mouth

def main():

    ears = Ears()
    brain = Brain()
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