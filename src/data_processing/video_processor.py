import cv2
import numpy as np

class VideoProcessor:
    def __init__(self, width=1280, height=720):
        """Initialize video processor with target dimensions"""
        self.target_width = width
        self.target_height = height
        
    def process_video_stream(self, video_path):
        """Process video file and yield frames"""
        cap = cv2.VideoCapture(video_path)
        
        try:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                    
                # Resize frame to target dimensions
                frame = cv2.resize(frame, (self.target_width, self.target_height))
                yield frame
                
        finally:
            cap.release()