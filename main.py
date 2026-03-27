import os
import logging

from config import (
    JARVIS_NAME,
    EXIT_COMMANDS,
    DEACTIVATE_COMMANDS,
    ACTIVATE_COMMANDS,
    TEXT_MODE,
    VOICE_MODE,
)

from voice.listener import Listener
from voice.tts_engine import TextToSpeech

from core.brain import Brain
from core.wake_word import detect_wake_word

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/jarvis.log",
    level=logging.ERROR
)


def initialize():

    listener = Listener() if VOICE_MODE else None
    tts = TextToSpeech()
    brain = Brain()

    print("\n[JARVIS SYSTEM STARTED]\n")

    tts.speak("Jarvis system started")

    return listener, tts, brain


listener, tts, brain = initialize()


while True:

    try:

        command = None

        # TEXT MODE
        if TEXT_MODE:
            command = input("You > ")

        # VOICE MODE
        elif VOICE_MODE and listener:
            command = listener.listen()

        if not command:
            continue

        command = command.lower().strip()
        
        # EXIT
        if command in EXIT_COMMANDS:

            print("Jarvis > Shutting down")
            tts.speak("Jarvis system shutting down")
            break

        # ACTIVATE
        if command in ACTIVATE_COMMANDS:

            brain.state.activate()

            print("Jarvis > Activated")
            tts.speak("Jarvis activated")
            continue

        # DEACTIVATE
        if command in DEACTIVATE_COMMANDS:

            brain.state.sleep()

            print("Jarvis > Deactivated")
            tts.speak("Jarvis deactivated")
            continue

        # WAKE WORD
        if detect_wake_word(command):

            brain.state.activate()

            command = command.replace(JARVIS_NAME, "", 1).strip()

            if not command:
                continue

        # IGNORE if sleeping
        if not brain.state.is_active():
            continue

        response = brain.process(command)

        if response:

            print(f"Jarvis > {response}")
            tts.speak(response)

    except KeyboardInterrupt:

        print("\nJarvis > Shutting down")
        tts.speak("Jarvis shutting down")
        break

    except Exception as e:

        logging.error(f"Runtime error: {e}")