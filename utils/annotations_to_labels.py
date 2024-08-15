import os
import xml.etree.ElementTree as ET


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0 * dw
    y = (box[2] + box[3]) / 2.0 * dh
    w = (box[1] - box[0]) * dw
    h = (box[3] - box[2]) * dh
    return (x, y, w, h)


def convert_annotation(image_id):
    in_file = open('yolo/dataset/annotations/%s.xml' % (image_id))
    out_file = open('yolo/dataset/labels/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),
             float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(
            str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n'
            )


if __name__ == "__main__":
    if not os.path.exists('yolo/dataset/labels/'):
        os.makedirs('yolo/dataset/labels/')

    classes = ["quail"]

    for image_file in os.listdir('yolo/dataset/images'):
        if image_file.endswith('.jpg'):
            image_id = image_file[:-4]
            convert_annotation(image_id)
