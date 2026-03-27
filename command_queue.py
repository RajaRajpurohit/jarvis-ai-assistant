import time


class CommandQueue:

    def __init__(self):

        self.last_command = None
        self.last_time = 0
        self.cooldown = 5  # seconds

    def allow(self, command):

        now = time.time()

        if command == self.last_command:

            if now - self.last_time < self.cooldown:
                return False

        self.last_command = command
        self.last_time = now

        return True