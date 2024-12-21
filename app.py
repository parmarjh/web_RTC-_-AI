from flask import Flask
from src.ai.youth_genetic_ai import YouthGeneticAI
from src.telecalling.telecall import Telecall
from src.telecalling.telecall_handler import TelecallHandler
from src.video_calling.video_call import VideoCall
from src.video_calling.video_call_handler import VideoCallHandler
from src.messaging.message import Message
from src.messaging.message_handler import MessageHandler
from src.mix_calls.mix_call import MixCall
from src.mix_calls.mix_call_handler import MixCallHandler

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

# Add routes for telecalling, video calling, messaging, and mixed calls here

if __name__ == '__main__':
    app.run(debug=True)