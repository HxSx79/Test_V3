import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Upload folder for video files
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')

# YOLO model path
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'yolov11.pt')

# BOM file path
BOM_FILE = os.path.join(BASE_DIR, 'data', 'BOM.xlsx')

# Allowed file extensions
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv'}

# Flask configuration
SECRET_KEY = 'your-secret-key-here'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size