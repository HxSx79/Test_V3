import cv2
import numpy as np

class LineCrossingDetector:
    def __init__(self):
        """Initialize line crossing detector"""
        self.previous_positions = {}
        
    def detect_crossing(self, object_id, current_position, frame_width):
        """Detect if an object has crossed the center line"""
        center_line = frame_width // 2
        x, y = current_position
        
        if object_id in self.previous_positions:
            prev_x, _ = self.previous_positions[object_id]
            
            # Check if object crossed the center line
            if (prev_x < center_line and x >= center_line) or \
               (prev_x > center_line and x <= center_line):
                self.previous_positions[object_id] = (x, y)
                return 'crossed'
        
        self.previous_positions[object_id] = (x, y)
        return None
        
    def draw_line(self, frame):
        """Draw the center line on the frame"""
        height, width = frame.shape[:2]
        center_x = width // 2
        
        cv2.line(frame, (center_x, 0), (center_x, height), 
                (0, 255, 255), 2)
        
        return frame