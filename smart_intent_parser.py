import re


class SmartIntentParser:

    def __init__(self):

        self.noise_words = {
            "please", "could", "would", "can",
            "you", "for", "me", "hey", "hi"
        }

        self.synonyms = {

            "launch": "open",
            "start": "open",
            "run": "open",
            "khol": "open",
            "kholo": "open",

            "find": "search",
            "look": "search",
            "google": "search",

            "play": "play",

            "tell": "tell",
            "show": "show",
            "batao": "tell",
            "dikhao": "show"
        }

    def clean(self, command):

        words = command.split()

        filtered = []

        for w in words:

            if w in self.noise_words:
                continue

            filtered.append(w)

        return " ".join(filtered)

    def normalize(self, command):

        words = command.strip().split()

        if not words:
            return command

        first = words[0]

        if first in self.synonyms:
            words[0] = self.synonyms[first]

        return " ".join(words)

    def parse(self, command):

        command = command.lower()

        command = self.clean(command)

        command = self.normalize(command)

        command = re.sub(r"\s+", " ", command)

        return command.strip()