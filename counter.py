class LineCounter:

    def __init__(self):

        self.line_y = 600

        self.up_count = 0
        self.down_count = 0

        self.previous_positions = {}

        self.counted_ids = set()

    def update(self, tracked_objects):

        for obj in tracked_objects:

            x1, y1, x2, y2, object_id = obj

            center_y = (y1 + y2) // 2

            if object_id in self.previous_positions:

                previous_y = self.previous_positions[object_id]

                if object_id not in self.counted_ids:

                    # Up -> Down
                    if previous_y < self.line_y and center_y >= self.line_y:

                        self.down_count += 1
                        self.counted_ids.add(object_id)

                    # Down -> Up
                    elif previous_y > self.line_y and center_y <= self.line_y:

                        self.up_count += 1
                        self.counted_ids.add(object_id)

            self.previous_positions[object_id] = center_y

        return self.up_count, self.down_count