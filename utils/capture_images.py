import cv2
import os


def capture_images(output_dir, num_images=50):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    existing_images = [f for f in os.listdir(output_dir) if f.endswith('.jpg')]
    count = len(existing_images)

    cap = cv2.VideoCapture(0)

    while count < num_images + len(existing_images):
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Webcam - Press Space to Capture', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord(' '):
            image_path = os.path.join(output_dir, f'image_{count:04d}.jpg')
            cv2.imwrite(image_path, frame)
            print(f"Imagem capturada: {image_path}")
            count += 1

        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    output_dir = 'yolo/dataset/images'
    num_images = 50
    capture_images(output_dir, num_images)
