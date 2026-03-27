import os
import importlib
import logging

from core.trigger_matcher import TriggerMatcher


class SkillManager:

    def __init__(self, skills_folder="skills"):

        self.skills_folder = skills_folder
        self.skills = {}

        self.matcher = TriggerMatcher()

        self.load_skills()

    def load_skills(self):

        for root, dirs, files in os.walk(self.skills_folder):

            for file in files:

                if not file.endswith(".py") or file.startswith("_"):
                    continue

                path = os.path.join(root, file)

                module_path = path.replace("\\", ".").replace("/", ".")[:-3]

                try:

                    module = importlib.import_module(module_path)

                    if not hasattr(module, "Skill"):
                        continue

                    skill = module.Skill()

                    if not hasattr(skill, "name"):
                        continue

                    if not hasattr(skill, "triggers"):
                        skill.triggers = []

                    self.skills[skill.name] = skill

                except Exception as e:

                    logging.error(f"Skill load error {file}: {e}")

    def find_skill(self, command):

        for name, skill in self.skills.items():

            triggers = getattr(skill, "triggers", [])

            if not triggers:
                continue

            if self.matcher.match(command, triggers):
                return name

        return None

    def execute(self, skill_name, command, context=None):

        skill = self.skills.get(skill_name)

        if not skill:
            return None

        try:
            return skill.execute(command, context)

        except Exception as e:
            logging.error(f"Skill error {skill_name}: {e}")
            return None