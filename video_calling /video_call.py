class VideoCall:
    def __init__(self):
        self.is_active = False
        self.video_enabled = False

    def start_call(self):
        if not self.is_active:
            self.is_active = True
            print("Video call started.")

    def end_call(self):
        if self.is_active:
            self.is_active = False
            print("Video call ended.")

    def toggle_video(self):
        self.video_enabled = not self.video_enabled
        status = "enabled" if self.video_enabled else "disabled"
        print(f"Video is now {status}.")

    def get_call_status(self):
        return {
            "is_active": self.is_active,
            "video_enabled": self.video_enabled
        }
