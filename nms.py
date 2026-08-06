def calculate_iou(box1, box2):

    x1A, y1A, x2A, y2A = box1
    x1B, y1B, x2B, y2B = box2

    left = max(x1A, x1B)
    top = max(y1A, y1B)
    right = min(x2A, x2B)
    bottom = min(y2A, y2B)

    width = max(0, right - left)
    height = max(0, bottom - top)

    intersection = width * height

    areaA = (x2A - x1A) * (y2A - y1A)
    areaB = (x2B - x1B) * (y2B - y1B)

    union = areaA + areaB - intersection

    if union == 0:
        return 0

    return intersection / union


def manual_nms(boxes, scores, iou_threshold):

    keep = []

    indices = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )

    while indices:

        current = indices.pop(0)

        keep.append(current)

        new_indices = []

        for i in indices:

            iou = calculate_iou(boxes[current], boxes[i])

            if iou < iou_threshold:

                new_indices.append(i)

        indices = new_indices

    return keep