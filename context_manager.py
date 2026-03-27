class ContextManager:

    def __init__(self):

        self.pending_intent = None

    def set_pending(self, intent):

        self.pending_intent = intent

    def clear(self):

        self.pending_intent = None

    def has_pending(self):

        return self.pending_intent is not None