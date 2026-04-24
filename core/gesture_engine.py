class GestureEngine:
    def __init__(self):
        self.prev_gesture = None

    def get_gesture(self, landmarks):
        if not landmarks:
            return None

        # Example: index finger up
        index_tip = landmarks[8]
        middle_tip = landmarks[12]

        if index_tip.y < middle_tip.y:
            return "POINT"

        return "UNKNOWN"