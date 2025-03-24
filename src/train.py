import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Set dataset path
dataset_path = "dataset/"

# Image preprocessing
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_generator = datagen.flow_from_directory(dataset_path, target_size=(150, 150),
                                              batch_size=32, class_mode='categorical',
                                              subset='training')

val_generator = datagen.flow_from_directory(dataset_path, target_size=(150, 150),
                                            batch_size=32, class_mode='categorical',
                                            subset='validation')

# Model Architecture
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(150,150,3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(6, activation='softmax')  # 6 categories
])

# Compile Model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train Model
model.fit(train_generator, validation_data=val_generator, epochs=10)

# Save Model
model.save("models/waste_classifier.h5")
