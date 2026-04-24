import pyautogui

class ActionController:
    def execute(self, gesture, position=None):
        if gesture == "POINT" and position:
            pyautogui.moveTo(position[0], position[1])

        elif gesture == "CLICK":
            pyautogui.click()