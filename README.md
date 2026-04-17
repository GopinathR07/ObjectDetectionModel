# 🎯 AI Object Detection Web App

A powerful **Object Detection Web Application** built using **YOLOv8** and **Streamlit** that allows users to detect real-world objects from images instantly.

---

## 🚀 Live Demo

👉 *(Add your Streamlit deployment link here after hosting)*

---

## 📸 Features

* 📤 Upload images for object detection
* 📷 Capture images using webcam (browser-based)
* 🎯 Detect multiple objects with bounding boxes
* 📊 Adjustable confidence threshold
* ⚡ Fast and efficient YOLOv8 inference
* 🌐 Deployed as a web application

---

## 🧠 Tech Stack

* **Python**
* **Streamlit** – Web UI framework
* **YOLOv8 (Ultralytics)** – Object detection model
* **OpenCV** – Image processing
* **PyTorch** – Deep learning backend
* **NumPy & PIL** – Image handling

---

## 📂 Project Structure

```text
object-detection-app/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── .gitignore          # Ignore unnecessary files
```

---

## ⚙️ Installation & Setup

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/object-detection-app.git
cd object-detection-app
```

---

### 🔹 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 3. Run the Application

```bash
streamlit run app.py
```

---

## 🧪 How It Works

1. User uploads or captures an image
2. Image is processed using YOLOv8 model
3. Model detects objects with bounding boxes
4. Results are displayed in the web interface

---

## 📌 Notes

* The model (`yolov8n.pt`) is automatically downloaded on first run
* Webcam works via browser (not OpenCV window)
* Performance depends on CPU/GPU availability

---

## 📈 Future Improvements

* 🎥 Real-time video detection
* 🎯 Object tracking system
* 📊 Detection analytics dashboard
* 🌐 Deployment with custom domain

---

## 👨‍💻 Author

**Gopinath R**

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
