from core.camera import Camera
from core.hand_tracker import HandTracker
from utils.smoothing import Smoother

import pyautogui
import cv2
import time
import math

# Init
cam = Camera(640, 480)
tracker = HandTracker()
smooth = Smoother()

screen_w, screen_h = pyautogui.size()

last_click = 0
dragging = False

while True:
    frame = cam.get_frame()
    if frame is None:
        continue

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    result = tracker.process(frame)

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        landmarks = hand.landmark

        # --- Bounding Box ---
        margin = 100
        cv2.rectangle(frame, (margin, margin), (w - margin, h - margin), (0,255,0), 2)

        # Index finger
        x = int(landmarks[8].x * w)
        y = int(landmarks[8].y * h)

        # Clamp inside box
        x = max(margin, min(x, w - margin))
        y = max(margin, min(y, h - margin))

        # Normalize
        nx = (x - margin) / (w - 2 * margin)
        ny = (y - margin) / (h - 2 * margin)

        px = int(nx * screen_w)
        py = int(ny * screen_h)

        # Smooth
        sx, sy = smooth.smooth(px, py)

        # Move cursor
        pyautogui.moveTo(sx, sy)

        # Draw cursor
        cv2.circle(frame, (x, y), 10, (255, 0, 0), -1)

        # --- Pinch Detection ---
        index_tip = landmarks[8]
        thumb_tip = landmarks[4]

        distance = math.hypot(index_tip.x - thumb_tip.x,
                              index_tip.y - thumb_tip.y)

        # --- Click ---
        if distance < 0.03:
            if time.time() - last_click > 0.7:
                pyautogui.click()
                last_click = time.time()
                cv2.putText(frame, "CLICK", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # --- Drag ---
        if distance < 0.025:
            if not dragging:
                pyautogui.mouseDown()
                dragging = True
        else:
            if dragging:
                pyautogui.mouseUp()
                dragging = False

    cv2.imshow("Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()