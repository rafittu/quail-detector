import os
import random


def create_split(image_dir, train_file, test_file, test_ratio=0.2):
    images = [
        os.path.join(image_dir, f) for f in os.listdir(image_dir)
        if f.endswith('.jpg')
        ]
    random.shuffle(images)
    split_index = int(len(images) * (1 - test_ratio))
    train_images = images[:split_index]
    test_images = images[split_index:]

    with open(train_file, 'w') as f:
        f.write('\n'.join(train_images) + '\n')

    with open(test_file, 'w') as f:
        f.write('\n'.join(test_images) + '\n')


if __name__ == "__main__":
    create_split('yolo/dataset/images', 'yolo/train.txt', 'yolo/test.txt')
