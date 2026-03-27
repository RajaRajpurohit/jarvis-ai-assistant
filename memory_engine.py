import json
import os
import logging


class MemoryEngine:

    def __init__(self, memory_folder="memory"):

        self.memory_folder = memory_folder

        self.conversation_file = os.path.join(memory_folder, "conversation_memory.json")
        self.facts_file = os.path.join(memory_folder, "learned_facts.json")
        self.family_file = os.path.join(memory_folder, "family_tree.json")

        self._ensure_files()

    # ==================================
    # FILE SETUP
    # ==================================

    def _ensure_files(self):

        if not os.path.exists(self.memory_folder):
            os.makedirs(self.memory_folder)

        for file in [
            self.conversation_file,
            self.facts_file,
            self.family_file
        ]:

            if not os.path.exists(file):
                with open(file, "w") as f:
                    json.dump([], f)

    # ==================================
    # READ JSON
    # ==================================

    def _read(self, file):

        try:

            with open(file, "r") as f:
                return json.load(f)

        except Exception as e:

            logging.error(f"Memory read error: {e}")
            return []

    # ==================================
    # WRITE JSON
    # ==================================

    def _write(self, file, data):

        try:

            with open(file, "w") as f:
                json.dump(data, f, indent=4)

        except Exception as e:

            logging.error(f"Memory write error: {e}")

    # ==================================
    # REMEMBER CONVERSATION
    # ==================================

    def remember(self, command, response):

        history = self._read(self.conversation_file)

        history.append({
            "command": command,
            "response": response
        })

        history = history[-100:]

        self._write(self.conversation_file, history)

    # ==================================
    # GET HISTORY
    # ==================================

    def get_history(self):

        return self._read(self.conversation_file)

    # ==================================
    # STORE FACT
    # ==================================

    def store_fact(self, fact):

        facts = self._read(self.facts_file)

        facts.append(fact)

        self._write(self.facts_file, facts)

    # ==================================
    # STORE FAMILY MEMBER
    # ==================================

    def add_family_member(self, relation, name):

        family = self._read(self.family_file)

        family.append({
            "relation": relation,
            "name": name
        })

        self._write(self.family_file, family)

    # ==================================
    # GET FAMILY
    # ==================================

    def get_family(self):

        return self._read(self.family_file)