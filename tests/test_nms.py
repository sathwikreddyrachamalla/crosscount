from nms import calculate_iou, manual_nms


def test_iou_same_box():
    box = [0, 0, 100, 100]
    assert calculate_iou(box, box) == 1.0


def test_iou_no_overlap():
    box1 = [0, 0, 100, 100]
    box2 = [200, 200, 300, 300]
    assert calculate_iou(box1, box2) == 0.0


def test_manual_nms():
    boxes = [
        [0, 0, 100, 100],
        [10, 10, 110, 110],
        [200, 200, 300, 300]
    ]

    scores = [0.9, 0.8, 0.95]

    keep = manual_nms(boxes, scores, 0.5)

    assert len(keep) == 2