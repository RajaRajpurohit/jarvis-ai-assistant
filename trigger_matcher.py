class TriggerMatcher:

    def match(self, command, triggers):

        if not command:
            return False

        command = command.lower().strip()

        for trigger in triggers:

            trigger = trigger.lower().strip()

            # exact match
            if command == trigger:
                return True

            # command contains trigger
            if trigger in command:
                return True

        return False