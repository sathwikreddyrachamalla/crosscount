# CrossCount – People Counting using YOLOv8

## Overview

CrossCount is a computer vision project that detects, tracks, and counts people crossing a predefined line in a video.

The project uses the YOLOv8 object detection model to detect people, a manually implemented Non-Maximum Suppression (NMS) algorithm to remove duplicate detections, a simple centroid-based tracker to assign IDs, and a line-crossing counter to count unique people.

---

## Features

- Person detection using YOLOv8
- Manual Non-Maximum Suppression (NMS)
- Bounding box visualization
- Object tracking with unique IDs
- Horizontal line-crossing counter
- Live people count display
- Output video generation

---

## Project Structure

```
crosscount/
│── detector.py      # YOLO person detection
│── tracker.py       # Object tracking
│── counter.py       # Line crossing counter
│── nms.py           # Manual Non-Maximum Suppression
│── run.py           # Main program
│── input_video.mp4
│── output_video.mp4
│── yolov8n.pt
│── README.md
```

---

## Requirements

Install the required packages:

```bash
pip install ultralytics opencv-python
```

---

## How to Run

Run the project using:

```bash
python run.py
```

Press **Q** to quit the video.

---

## Workflow

```
Input Video
     │
     ▼
YOLOv8 Detection
     │
     ▼
Manual NMS
     │
     ▼
Tracker
     │
     ▼
Line Counter
     │
     ▼
Annotated Output Video
```

---

## Technologies Used

- Python
- OpenCV
- Ultralytics YOLOv8

---

## Manual NMS

A custom Non-Maximum Suppression algorithm was implemented instead of relying only on the detector output.

The algorithm:

- Calculates IoU between bounding boxes.
- Sorts detections by confidence.
- Removes overlapping duplicate boxes.
- Keeps only the highest-confidence detection.

---

## Tracking

A simple centroid-distance tracker is used.

The tracker:

- Computes the center of each bounding box.
- Matches detections between consecutive frames.
- Assigns unique IDs.
- Creates new IDs for newly detected objects.

---

## Counting Logic

A horizontal counting line is placed in the video.

When the center of a tracked object crosses the line for the first time:

- The object ID is stored.
- The counter increases by one.
- The same object is not counted again.

---

## Future Improvements

- Replace the basic tracker with DeepSORT or ByteTrack.
- Improve counting accuracy in crowded scenes.
- Support multiple counting zones.
- Add real-time webcam support.

---

## Author

Shiva Sathwik Reddy