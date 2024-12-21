class MixCall:
    def __init__(self):
        self.active_calls = []

    def add_call(self, call):
        self.active_calls.append(call)

    def remove_call(self, call):
        if call in self.active_calls:
            self.active_calls.remove(call)

    def get_active_calls(self):
        return self.active_calls

    def clear_calls(self):
        self.active_calls.clear()

    def mix_calls(self):
        # Logic to combine different types of calls into a single session
        pass

    def end_mix_call(self):
        # Logic to end the mixed call session
        self.clear_calls()
