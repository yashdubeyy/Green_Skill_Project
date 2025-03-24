import tensorflow as tf
import numpy as np
import cv2
import sys

# Load trained model
model = tf.keras.models.load_model("models/waste_classifier.h5")

# Waste categories
categories = ['Cardboard', 'Glass', 'Metal', 'Paper', 'Plastic', 'Trash']

def classify_waste(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (150,150))
    img = img / 255.0  # Normalize
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)
    predicted_class = np.argmax(prediction)
    
    return categories[predicted_class]

if __name__ == "__main__":
    image_path = sys.argv[1]
    print(f"Predicted Waste Type: {classify_waste(image_path)}")
