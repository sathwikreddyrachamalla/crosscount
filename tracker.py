class Tracker:

    def __init__(self):

        self.next_id = 0
        self.objects = {}

    def update(self, detections):

        tracked_objects = []
        new_objects = {}

        for detection in detections:

            x1, y1, x2, y2 = detection

            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            object_id = None

            for old_id, (old_cx, old_cy) in self.objects.items():

                distance = ((cx - old_cx) ** 2 + (cy - old_cy) ** 2) ** 0.5

                if distance < 50:
                    object_id = old_id
                    break

            if object_id is None:
                object_id = self.next_id
                self.next_id += 1

            new_objects[object_id] = (cx, cy)
            tracked_objects.append([x1, y1, x2, y2, object_id])

        self.objects = new_objects

        return tracked_objects