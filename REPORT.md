# CrossCount Project Report

## 1. Project Title

CrossCount – People Detection, Tracking and Line Crossing Counter using YOLOv8

---

## 2. Objective

The objective of this project is to detect people in a video, track each person using a unique ID, and count the number of people crossing a predefined line.

---

## 3. Tools and Technologies

- Python
- OpenCV
- Ultralytics YOLOv8
- VS Code

---

## 4. Project Workflow

Input Video

↓

YOLOv8 Person Detection

↓

Manual Non-Maximum Suppression (NMS)

↓

Centroid-Based Object Tracking

↓

Line Crossing Counter

↓

Output Video

---

## 5. Implementation

### Person Detection

YOLOv8 is used to detect people in every frame of the input video. Only the "person" class is considered for further processing.

### Manual NMS

A custom Non-Maximum Suppression algorithm was implemented to remove duplicate bounding boxes. The algorithm calculates the Intersection over Union (IoU) between boxes and retains only the highest-confidence detections.

### Object Tracking

A simple centroid-based tracker assigns a unique ID to each detected person. The tracker compares the center points of objects between consecutive frames and reuses IDs when the distance is below a threshold.

### Line Counter

A horizontal counting line is drawn on the video. When the center of a tracked person crosses the line for the first time, the person's ID is stored and the counter is incremented. Duplicate counting is avoided using the stored IDs.

---

## 6. Challenges Faced

- Understanding YOLO detection output.
- Implementing IoU calculation correctly.
- Writing Manual NMS from scratch.
- Maintaining object IDs across frames.
- Avoiding duplicate counting.

---

## 7. Results

The final system successfully:

- Detects people using YOLOv8.
- Applies Manual NMS.
- Tracks people with unique IDs.
- Counts people crossing a horizontal line.
- Displays the live count on the video.
- Generates an annotated output video.

---

## 8. Future Improvements

- Use DeepSORT or ByteTrack for more robust tracking.
- Improve counting accuracy in crowded scenes.
- Support multiple counting lines.
- Add real-time webcam support.

---

## 9. Conclusion

The CrossCount project successfully combines object detection, manual Non-Maximum Suppression, tracking, and counting into a complete computer vision pipeline. The project demonstrates practical knowledge of OpenCV, YOLOv8, tracking algorithms, and object counting.