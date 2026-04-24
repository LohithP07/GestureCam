# GestureCam -- Virtual Mouse Using Hand Tracking (v1)

## 🚀 Overview

GestureCam is a real-time computer vision project that turns your webcam
into a **gesture-controlled virtual mouse**. Using hand tracking, you
can move the cursor, click, and drag---all without touching a physical
mouse.

This is **Version 1 (Initial Release)**, focused on building a stable,
usable foundation with smooth tracking and basic gestures.

---

## ✨ Features (v1)

- 🖱️ **Cursor Control**
  - Move your mouse using your index finger
  - Controlled within a defined on-screen region for better
    precision
- 🤏 **Click Gesture**
  - Pinch (thumb + index finger) to perform a click
  - Built-in cooldown to prevent accidental multiple clicks
- ✊ **Drag & Drop**
  - Hold pinch to drag items
  - Release pinch to drop
- 🎯 **Bounding Control Area**
  - Movement restricted to a central box for stability and accuracy
- 🧊 **Dynamic Smoothing**
  - Slow movements → precise control\
  - Fast movements → responsive tracking

---

## 🧠 How It Works

1.  Webcam captures video frames\
2.  Hand landmarks are detected using MediaPipe\
3.  Index finger position is tracked\
4.  Coordinates are mapped to screen space\
5.  Gestures (pinch) trigger mouse actions

---

## 🛠️ Tech Stack

- Python 3.10\
- OpenCV\
- MediaPipe\
- PyAutoGUI

---

## 📁 Project Structure

gesture_control/ │ ├── main.py │ ├── core/ │ ├── camera.py │ ├──
hand_tracker.py │ ├── utils/ │ ├── smoothing.py │ ├── features/ │ ├──
virtual_mouse.py

---

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone https://github.com/yourusername/gesturecam.git\
cd gesturecam

### 2. Create virtual environment (Python 3.10 required)

py -3.10 -m venv venv310\
venv310`\Scripts`{=tex}`\activate  `{=tex}

### 3. Install dependencies

pip install opencv-python mediapipe pyautogui

### 4. Run the project

python main.py

---

## 🎮 Controls

Gesture Action

---

☝️ Index finger move Move cursor
🤏 Pinch (quick) Click
🤏 Hold pinch Drag
✋ Outside control box Ignored

---

## ⚠️ Requirements

- Python **3.10** (MediaPipe compatibility)
- Webcam
- Good lighting conditions

---

## 🧪 Known Limitations (v1)

- Click vs drag distinction may feel sensitive\
- Performance depends on lighting and camera quality\
- No gesture customization yet

---

## 🔮 Future Improvements

- Scroll gesture (two fingers)\
- Gesture customization system\
- Mode switching (mouse vs shortcuts)\
- Performance optimization (higher FPS)\
- Multi-hand support

---

## 📌 Version

**v1.0 -- Initial Release**

---

## 🤝 Contributing

Contributions, ideas, and improvements are welcome.

---

## 📄 License

MIT License (or your preferred license)
