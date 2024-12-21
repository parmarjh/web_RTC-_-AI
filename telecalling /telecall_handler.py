from flask import Flask, request, jsonify

class TelecallHandler:
    def __init__(self):
        self.active_calls = {}

    def initiate_call(self, caller_id, receiver_id):
        if receiver_id in self.active_calls:
            return jsonify({"error": "Receiver is already in a call."}), 400
        self.active_calls[receiver_id] = caller_id
        return jsonify({"message": "Call initiated.", "caller": caller_id, "receiver": receiver_id}), 200

    def end_call(self, caller_id, receiver_id):
        if receiver_id not in self.active_calls or self.active_calls[receiver_id] != caller_id:
            return jsonify({"error": "No active call found."}), 404
        del self.active_calls[receiver_id]
        return jsonify({"message": "Call ended.", "caller": caller_id, "receiver": receiver_id}), 200

    def get_active_calls(self):
        return jsonify(self.active_calls), 200

# Example usage
app = Flask(__name__)
telecall_handler = TelecallHandler()

@app.route('/telecall/initiate', methods=['POST'])
def initiate_call():
    data = request.json
    return telecall_handler.initiate_call(data['caller_id'], data['receiver_id'])

@app.route('/telecall/end', methods=['POST'])
def end_call():
    data = request.json
    return telecall_handler.end_call(data['caller_id'], data['receiver_id'])

@app.route('/telecall/active', methods=['GET'])
def active_calls():
    return telecall_handler.get_active_calls()

if __name__ == '__main__':
    app.run(debug=True)
