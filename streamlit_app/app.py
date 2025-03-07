import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image

# Load trained model
model = tf.keras.models.load_model("models/waste_classifier.h5")

# Waste categories
categories = ['Cardboard', 'Glass', 'Metal', 'Paper', 'Plastic', 'Trash']

def classify_waste(image):
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    img = cv2.resize(img, (150,150))
    img = img / 255.0  # Normalize
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)
    predicted_class = np.argmax(prediction)
    
    return categories[predicted_class]

# Streamlit UI
st.title("AI-Powered Waste Classifier")
st.write("Upload an image to classify the type of waste.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Classify"):
        result = classify_waste(image)
        st.success(f"Predicted Waste Type: {result}")
