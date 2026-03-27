from core.skill_manager import SkillManager
from core.state_manager import StateManager
from core.command_queue import CommandQueue
from core.command_splitter import CommandSplitter
from core.context_manager import ContextManager


class Brain:

    def __init__(self):

        self.skills = SkillManager()

        self.state = StateManager()

        self.queue = CommandQueue()

        self.splitter = CommandSplitter()

        self.context = ContextManager()

    def process(self, command):

        if not command:
            return None

        commands = self.splitter.split(command)

        responses = []

        for cmd in commands:

            if not self.queue.allow(cmd):
                responses.append("Ignoring duplicate command")
                continue

            # check for pending context
            if self.context.has_pending():

                intent = self.context.pending_intent

                cmd = f"{intent} {cmd}"

                self.context.clear()

            skill_name = self.skills.find_skill(cmd)

            if not skill_name:

                responses.append("I don't know that command yet.")
                continue

            result = self.skills.execute(skill_name, cmd)

            if result:

                responses.append(result)

        if not responses:
            return None

        return "\n".join(responses)