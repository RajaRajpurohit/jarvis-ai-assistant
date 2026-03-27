import json
import os
import logging


class LearningEngine:

    def __init__(self, file_path="memory/custom_commands.json"):

        self.file_path = file_path
        self._ensure_file()

    # ==================================
    # FILE SETUP
    # ==================================

    def _ensure_file(self):

        folder = os.path.dirname(self.file_path)

        if not os.path.exists(folder):
            os.makedirs(folder)

        if not os.path.exists(self.file_path):

            with open(self.file_path, "w") as f:
                json.dump({}, f)

    # ==================================
    # READ
    # ==================================

    def _read(self):

        try:

            with open(self.file_path, "r") as f:
                return json.load(f)

        except Exception as e:

            logging.error(f"Learning read error: {e}")
            return {}

    # ==================================
    # WRITE
    # ==================================

    def _write(self, data):

        try:

            with open(self.file_path, "w") as f:
                json.dump(data, f, indent=4)

        except Exception as e:

            logging.error(f"Learning write error: {e}")

    # ==================================
    # LEARN COMMAND
    # ==================================

    def learn(self, command, steps):

        data = self._read()

        data[command] = steps

        self._write(data)

    # ==================================
    # GET COMMAND
    # ==================================

    def get_command(self, command):

        data = self._read()

        return data.get(command)

    # ==================================
    # EXECUTE LEARNED COMMAND
    # ==================================

    def execute(self, command, brain):

        data = self._read()

        steps = data.get(command)

        if not steps:
            return None

        responses = []

        for step in steps:

            response = brain.process(step)

            if response:
                responses.append(response)

        return " ".join(responses)