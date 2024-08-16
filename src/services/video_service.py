import cv2


class VideoService:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def show_frame(self, frame, window_name='Video Stream'):
        cv2.imshow(window_name, frame)

    def wait_for_quit(self):
        return cv2.waitKey(1) & 0xFF == ord('q')
