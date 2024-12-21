from flask import jsonify, request

class MessageHandler:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, recipient, content):
        message = {
            'sender': sender,
            'recipient': recipient,
            'content': content,
            'status': 'sent'
        }
        self.messages.append(message)
        return jsonify({'message': 'Message sent successfully', 'data': message}), 200

    def receive_messages(self, recipient):
        received_messages = [msg for msg in self.messages if msg['recipient'] == recipient]
        return jsonify({'messages': received_messages}), 200

    def delete_message(self, message_id):
        if 0 <= message_id < len(self.messages):
            deleted_message = self.messages.pop(message_id)
            return jsonify({'message': 'Message deleted successfully', 'data': deleted_message}), 200
        return jsonify({'message': 'Message not found'}), 404

message_handler = MessageHandler()
