import base64
import cv2
import numpy as np
from flask_socketio import emit

class SocketHandler:
    def __init__(self, video_processor, object_detector, line_detector, bom_handler):
        self.video_processor = video_processor
        self.object_detector = object_detector
        self.line_detector = line_detector
        self.bom_handler = bom_handler

    def process_video(self, video_path):
        """Process video frames and emit detection results"""
        try:
            for frame in self.video_processor.process_video_stream(video_path):
                # Detect objects in the frame
                detections = self.object_detector.detect_objects(frame)
                
                # Draw center line
                frame = self.line_detector.draw_line(frame)
                
                # Process each detection
                crossing_events = []
                for obj_id, (class_name, bbox) in enumerate(detections):
                    x_center = (bbox[0] + bbox[2]) / 2
                    y_center = (bbox[1] + bbox[3]) / 2
                    
                    # Check if object crossed the line
                    if self.line_detector.detect_crossing(obj_id, (x_center, y_center), 
                                                        frame.shape[1]) == 'crossed':
                        # Get part information from BOM
                        bom_info = self.bom_handler.get_part_info(class_name)
                        crossing_events.append({
                            'object_id': obj_id,
                            'class_name': class_name,
                            'bom_info': bom_info
                        })
                
                # Convert frame to base64 for sending to client
                _, buffer = cv2.imencode('.jpg', frame)
                frame_base64 = base64.b64encode(buffer).decode('utf-8')
                
                # Emit detection update
                emit('detection_update', {
                    'frame': frame_base64,
                    'crossing_events': crossing_events
                })
                
        except Exception as e:
            emit('error', {'message': str(e)})