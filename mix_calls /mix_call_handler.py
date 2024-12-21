from flask import Flask, request, jsonify

class MixCallHandler:
    def __init__(self):
        self.active_calls = {}

    def start_mix_call(self, call_id, participants):
        if call_id in self.active_calls:
            return jsonify({"error": "Call already exists"}), 400
        self.active_calls[call_id] = participants
        return jsonify({"message": "Mixed call started", "call_id": call_id}), 200

    def end_mix_call(self, call_id):
        if call_id not in self.active_calls:
            return jsonify({"error": "Call not found"}), 404
        del self.active_calls[call_id]
        return jsonify({"message": "Mixed call ended", "call_id": call_id}), 200

    def get_active_calls(self):
        return jsonify({"active_calls": self.active_calls}), 200

mix_call_handler = MixCallHandler()
