import logging


class CommandRouter:

    def __init__(self, skill_manager):

        self.skill_manager = skill_manager
        self.intent_to_skill = {}

        logging.info("CommandRouter initialized")

        self._register_all_skills()

    # ====================================
    # REGISTER ALL SKILLS
    # ====================================

    def _register_all_skills(self):

        for skill in self.skill_manager.skills.values():

            self.register_skill(skill)

    # ====================================
    # REGISTER SKILL INTENTS
    # ====================================

    def register_skill(self, skill):

        skill_name = skill.name

        intents = getattr(skill, "intents", [])

        for intent in intents:

            intent = intent.lower().strip()

            self.intent_to_skill[intent] = skill_name

            logging.info(f"Intent '{intent}' → {skill_name}")

    # ====================================
    # ROUTE COMMAND
    # ====================================

    def route(self, command):

        command = command.lower().strip()

        # 1️⃣ DIRECT INTENT MATCH
        for intent, skill in self.intent_to_skill.items():

            if command.startswith(intent):
                return skill

        # 2️⃣ TRIGGER MATCH
        skill = self.skill_manager.find_skill(command)

        if skill:
            return skill

        return None