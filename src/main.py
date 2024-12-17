import os
from flask import Flask, render_template
from flask_socketio import SocketIO
from src.config.settings import SECRET_KEY, MODEL_PATH, BOM_FILE
from src.web.routes import bp
from src.web.socket_handler import SocketHandler
from src.data_processing.video_processor import VideoProcessor
from src.data_processing.bom_handler import BOMHandler
from src.detection.detector import ObjectDetector
from src.detection.line_detector import LineCrossingDetector

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
socketio = SocketIO(app)

# Register blueprints
app.register_blueprint(bp)

# Initialize components
video_processor = VideoProcessor()
object_detector = ObjectDetector(MODEL_PATH)
line_detector = LineCrossingDetector()
bom_handler = BOMHandler(BOM_FILE)

# Initialize socket handler
socket_handler = SocketHandler(
    video_processor=video_processor,
    object_detector=object_detector,
    line_detector=line_detector,
    bom_handler=bom_handler
)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@socketio.on('start_processing')
def handle_processing(data):
    """Handle video processing request"""
    video_path = data.get('video_path')
    if video_path and os.path.exists(video_path):
        socket_handler.process_video(video_path)
    else:
        socketio.emit('error', {'message': 'Invalid video path'})

if __name__ == '__main__':
    # Create required directories
    os.makedirs('src/static/uploads', exist_ok=True)
    
    # Run the application
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)