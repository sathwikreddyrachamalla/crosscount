import cv2
from detector import detect_people
from tracker import Tracker
from counter import LineCounter

video = cv2.VideoCapture("input_video.mp4")


tracker = Tracker()
counter = LineCounter()


fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(
    "output_video.mp4",
    fourcc,
    30,
    (
        int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    )
)

while True:

    ret, frame = video.read()

    if not ret:
        break


    detections = detect_people(frame)


    tracked_objects = tracker.update(detections)

    
    up_count, down_count = counter.update(tracked_objects)

    
    for obj in tracked_objects:

        x1, y1, x2, y2, object_id = obj

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"ID: {object_id}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )


    cv2.line(frame, (100, 600), (1000, 600), (0, 0, 255), 3)

    
    cv2.putText(
        frame,
        f"Up -> Down : {down_count}",
        (30, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

    cv2.putText(
        frame,
        f"Down -> Up : {up_count}",
        (30, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 0, 0),
        2
    )

    out.write(frame)


    cv2.imshow("CrossCount", frame)

    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


video.release()
out.release()
cv2.destroyAllWindows()