from ultralytics import YOLO
from nms import manual_nms

model = YOLO("yolov8n.pt")


def detect_people(frame):

    results = model(frame)

    boxes = []
    scores = []

    for box in results[0].boxes:

        class_id = int(box.cls[0])

        if class_id != 0:
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        boxes.append([x1, y1, x2, y2])
        scores.append(float(box.conf[0]))

    keep = manual_nms(boxes, scores, 0.5)

    detections = []

    for i in keep:
        detections.append(boxes[i])

    return detections