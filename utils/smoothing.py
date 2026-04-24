class Smoother:
    def __init__(self):
        self.prev_x = 0
        self.prev_y = 0

    def smooth(self, x, y):
        dx = abs(x - self.prev_x)
        dy = abs(y - self.prev_y)

        speed = dx + dy

        # Dynamic smoothing
        alpha = 0.1 if speed < 5 else 0.3

        sx = self.prev_x + alpha * (x - self.prev_x)
        sy = self.prev_y + alpha * (y - self.prev_y)

        self.prev_x, self.prev_y = sx, sy
        return int(sx), int(sy)