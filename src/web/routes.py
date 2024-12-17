from flask import Blueprint, request, jsonify
from src.utils.file_handler import allowed_file, save_uploaded_file

bp = Blueprint('routes', __name__)

@bp.route('/upload', methods=['POST'])
def upload_file():
    """Handle video file upload"""
    if 'video' not in request.files:
        return jsonify({'success': False, 'error': 'No file provided'})
        
    file = request.files['video']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No file selected'})
        
    if not allowed_file(file.filename):
        return jsonify({'success': False, 'error': 'Invalid file type'})
        
    try:
        file_path = save_uploaded_file(file)
        return jsonify({'success': True, 'video_path': file_path})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})