import re


# ==============================
# BASIC NORMALIZATION
# ==============================

def normalize_command(text):

    text = text.lower().strip()

    fixes = {

        "service": "jarvis",
        "jarviz": "jarvis",
        "jarves": "jarvis",

        "what type": "what time",
        "type is it": "time is it",

        "node pad": "notepad",
        "note pad": "notepad",

        # speech errors
        "pink": "ping",
        "von": "one",
        "too": "two",
        "to": "two",
        "minimise": "minimize",

        # math speech
        "into": "*",
        "multiply": "*",
        "times": "*",
        "plus": "+",
        "minus": "-",
        "divide": "/",
        "divided by": "/",
        "power": "**"

    }

    for wrong, correct in fixes.items():
        text = text.replace(wrong, correct)

    return text


# ==============================
# HINDI / HINGLISH SUPPORT
# ==============================

HINGLISH_MAP = {

    # open
    "kholo": "open",
    "khol": "open",
    "kholna": "open",
    "kholo na": "open",
    "chalu karo": "open",
    "chalu": "open",
    "start karo": "open",

    # close
    "band karo": "close",
    "band kar": "close",
    "band": "close",

    # search
    "dhundo": "search",
    "talash karo": "search",
    "google karo": "search",

    # show
    "dikhao": "show",
    "batao": "tell",
    "dikhana": "show",

    # weather
    "mausam": "weather",
    "temperature": "weather",
    "garmi": "weather",
    "thand": "weather",

    # news
    "khabar": "news",
    "samachar": "news",

    # gold / silver
    "sona": "gold",
    "sone ka": "gold",
    "chandi": "silver",

    # youtube
    "gaana": "music",
    "song": "music",

    # volume
    "awaz": "volume",
    "awaaz": "volume",
    "volume badhao": "volume up",
    "volume kam karo": "volume down",

    # screenshot
    "photo lo": "screenshot",
    "screen shot": "screenshot",

    # system
    "computer band": "shutdown computer",
    "computer restart": "restart computer",

}


def clean_hinglish(command):

    for word, replacement in HINGLISH_MAP.items():

        if word in command:
            command = command.replace(word, replacement)

    command = re.sub(r"\s+", " ", command)

    return command.strip()


# ==============================
# INDIAN NUMBER WORDS
# ==============================

NUMBER_WORDS = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ten": "10",

    "hundred": "100",
    "thousand": "1000",
    "lakh": "100000",
    "lac": "100000",
    "crore": "10000000"
}