import pip
from flask import Flask, request, jsonify
# pip install ai # type: ignore
from ai.youth_genetic_ai import YouthGeneticAI
from telecalling.telecall import Telecall
from telecalling.telecall_handler import TelecallHandler
from video_calling.video_call import VideoCall # type: ignore
from video_calling.video_call_handler import VideoCallHandler
from messaging.message import Message
from messaging.message_handler import MessageHandler
from mix_calls.mix_call import MixCall
from mix_calls.mix_call_handler import MixCallHandler

app = Flask(__name__)

# Initialize components
youth_genetic_ai = YouthGeneticAI()
telecall = Telecall()
telecall_handler = TelecallHandler()
video_call = VideoCall()
video_call_handler = VideoCallHandler()
message = Message()
message_handler = MessageHandler()
mix_call = MixCall()
mix_call_handler = MixCallHandler()

@app.route('/')
def home():
    return "Welcome to the WebRTC-based application!"

# Add routes for telecalling
@app.route('/telecall/initiate', methods=['POST'])
def initiate_telecall():
    data = request.json
    return telecall_handler.initiate_call(data['caller_id'], data['receiver_id'])

@app.route('/telecall/end', methods=['POST'])
def end_telecall():
    data = request.json
    return telecall_handler.end_call(data['caller_id'], data['receiver_id'])

@app.route('/telecall/active', methods=['GET'])
def active_telecalls():
    return telecall_handler.get_active_calls()

# Add routes for video calling
@app.route('/video_call/start', methods=['POST'])
def start_video_call():
    data = request.json
    return video_call_handler.start_video_call(data['call_id'], data['user_id'])

@app.route('/video_call/end', methods=['POST'])
def end_video_call():
    data = request.json
    return video_call_handler.end_video_call(data['call_id'])

@app.route('/video_call/toggle', methods=['POST'])
def toggle_video():
    data = request.json
    return video_call_handler.toggle_video(data['call_id'], data['user_id'])

# Add routes for messaging
@app.route('/message/send', methods=['POST'])
def send_message():
    data = request.json
    return message_handler.send_message(data['sender'], data['recipient'], data['content'])

@app.route('/message/receive', methods=['GET'])
def receive_messages():
    recipient = request.args.get('recipient')
    return message_handler.receive_messages(recipient)

@app.route('/message/delete', methods=['POST'])
def delete_message():
    data = request.json
    return message_handler.delete_message(data['message_id'])

# Add routes for mixed calls
@app.route('/mix_call/start', methods=['POST'])
def start_mix_call():
    data = request.json
    return mix_call_handler.start_mix_call(data['call_id'], data['participants'])

@app.route('/mix_call/end', methods=['POST'])
def end_mix_call():
    data = request.json
    return mix_call_handler.end_mix_call(data['call_id'])

@app.route('/mix_call/active', methods=['GET'])
def active_mix_calls():
    return mix_call_handler.get_active_calls()

if __name__ == '__main__':
    app.run(debug=True)