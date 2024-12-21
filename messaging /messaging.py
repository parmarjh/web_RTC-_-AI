class Message:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.timestamp = None  # To be set when the message is sent

    def send(self):
        # Logic to send the message
        self.timestamp = self._get_current_timestamp()
        # Code to send the message to the recipient

    def delete(self):
        # Logic to delete the message
        pass

    def _get_current_timestamp(self):
        from datetime import datetime
        return datetime.now().isoformat()

class MessageManager:
    def __init__(self):
        self.messages = []

    def receive_message(self, message):
        self.messages.append(message)
        # Logic to notify the recipient

    def get_messages_for_user(self, user):
        return [msg for msg in self.messages if msg.recipient == user]

    def delete_message(self, message):
        if message in self.messages:
            self.messages.remove(message)
            message.delete()  # Call the delete method of the Message class
