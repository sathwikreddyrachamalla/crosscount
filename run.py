import cv2
from detector import detect_people
from tracker import Tracker
from counter import LineCounter

# Open input video
video = cv2.VideoCapture("input_video.mp4")

# Create tracker and counter
tracker = Tracker()
counter = LineCounter()

# Create output video
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

    # Detect people
    detections = detect_people(frame)

    # Track people
    tracked_objects = tracker.update(detections)

    # Update counter
    up_count, down_count = counter.update(tracked_objects)

    # Draw boxes and IDs
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

    # Draw counting line
    cv2.line(frame, (100, 600), (1000, 600), (0, 0, 255), 3)

    # Show counts
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

    # Save frame
    out.write(frame)

    # Show video
    cv2.imshow("CrossCount", frame)

    # Quit on Q
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
video.release()
out.release()
cv2.destroyAllWindows()