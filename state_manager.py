class StateManager:

    ACTIVE = "active"
    SLEEPING = "sleeping"

    def __init__(self):
        self.state = self.SLEEPING

    def activate(self):
        self.state = self.ACTIVE

    def sleep(self):
        self.state = self.SLEEPING

    def is_active(self):
        return self.state == self.ACTIVE