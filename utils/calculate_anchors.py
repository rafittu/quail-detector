import os
import numpy as np
from sklearn.cluster import KMeans


def load_boxes_from_annotations(annotations_path):
    boxes = []
    for file_name in os.listdir(annotations_path):
        if file_name.endswith('.txt'):
            with open(os.path.join(annotations_path, file_name), 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if len(parts) == 5:
                        _, x_center, y_center, width, height = map(
                            float, parts
                            )
                        boxes.append((width, height))
    return np.array(boxes)


def calculate_anchors(boxes, img_width, img_height, num_anchors=9):
    kmeans = KMeans(n_clusters=num_anchors, random_state=0).fit(boxes)
    anchors = np.array(kmeans.cluster_centers_)

    anchors = sorted(anchors, key=lambda x: x[0] * x[1])

    anchors_scaled = anchors * np.array([img_width, img_height])

    anchors_scaled = anchors_scaled.astype(int)

    return anchors_scaled


def save_anchors(anchors, output_file):
    anchors_list = anchors.flatten().tolist()
    anchors_str = ",  ".join(
        [f"{anchors_list[i]},{anchors_list[i+1]}" for i in range(
            0, len(anchors_list), 2
            )]
        )

    with open(output_file, 'w') as file:
        file.write(anchors_str + '\n')


if __name__ == "__main__":
    annotations_path = 'yolo/dataset/labels'
    output_file = 'yolo/anchors.txt'
    num_anchors = 9
    img_width = 608
    img_height = 608

    boxes = load_boxes_from_annotations(annotations_path)

    anchors = calculate_anchors(boxes, img_width, img_height, num_anchors)

    save_anchors(anchors, output_file)
