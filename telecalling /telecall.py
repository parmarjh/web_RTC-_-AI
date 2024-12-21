class Telecall:
    def __init__(self):
        self.call_state = "idle"

    def initiate_call(self, recipient):
        if self.call_state == "idle":
            self.call_state = "calling"
            print(f"Initiating call to {recipient}...")
            # Logic to initiate the call
        else:
            print("Cannot initiate call, already in a call.")

    def end_call(self):
        if self.call_state != "idle":
            print("Ending call...")
            self.call_state = "idle"
            # Logic to end the call
        else:
            print("No active call to end.")

    def get_call_state(self):
        return self.call_state

    def toggle_mute(self):
        # Logic to toggle mute
        print("Toggling mute...")
