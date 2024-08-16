from services.video_service import VideoService
from models.detection_model import DetectionModel


class DetectionController:
    def __init__(self, config_path, weights_path, names_path, camera_index=0):
        self.video_service = VideoService(camera_index)
        self.model = DetectionModel(config_path, weights_path, names_path)

    def start_detection(self):
        while True:
            frame = self.video_service.get_frame()
            if frame is None:
                break

            processed_frame = self.model.detect_and_draw(frame)
            self.video_service.show_frame(processed_frame)

            if self.video_service.wait_for_quit():
                break

        self.video_service.release()
