import os
from dotenv import load_dotenv
from controllers.detection_controller import DetectionController


def main():
    load_dotenv()

    config_path = os.getenv("CONFIG_PATH")
    weights_path = os.getenv("WEIGHTS_PATH")
    names_path = os.getenv("NAMES_PATH")
    camera_index = int(os.getenv("CAMERA_INDEX", 0))

    controller = DetectionController(
        config_path, weights_path, names_path, camera_index
        )
    controller.start_detection()


if __name__ == "__main__":
    main()
