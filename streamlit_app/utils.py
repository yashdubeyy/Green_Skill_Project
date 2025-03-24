import numpy as np
import cv2

# Waste categories
CATEGORIES = ['Cardboard', 'Glass', 'Metal', 'Paper', 'Plastic', 'Trash']

def preprocess_image(image):
    """Preprocess the image for model prediction"""
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    img = cv2.resize(img, (150,150))  # Resize to match the model's input size
    img = img / 255.0  # Normalize
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

def get_prediction(model, image):
    """Predict the category of waste"""
    img = preprocess_image(image)
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction)
    return CATEGORIES[predicted_class]
