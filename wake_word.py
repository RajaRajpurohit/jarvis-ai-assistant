from config import WAKE_WORDS


def detect_wake_word(text):

    if not text:
        return False

    text = text.lower().strip()

    for wake in WAKE_WORDS:

        wake = wake.lower()

        if text.startswith(wake + " "):
            return True

        if text == wake:
            return True

    return False