class CommandSplitter:

    def split(self, command):

        if not command:
            return []

        command = command.lower()

        separators = [
            " and ",
            " then ",
            ","
        ]

        commands = [command]

        for sep in separators:

            new_commands = []

            for cmd in commands:
                new_commands.extend(cmd.split(sep))

            commands = new_commands

        return [c.strip() for c in commands if c.strip()]