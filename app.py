import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image

st.title("🎯 YOLO Object Detection (Colab Web App)")

model = YOLO("yolov8n.pt")

uploaded_file = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    st.image(image, caption="Original Image")

    if st.button("Detect Objects"):
        results = model(image_np)
        annotated = results[0].plot()

        annotated = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
        st.image(annotated, caption="Detected Image")
