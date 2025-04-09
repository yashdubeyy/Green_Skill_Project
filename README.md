# AI-Powered Waste Classification System

An AI-powered system designed to classify waste into appropriate categories using deep learning, aiding in effective waste management and recycling.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## 📖 Overview

The **AI-Powered Waste Classification System** is a deep learning-based application that categorizes waste materials based on image inputs. It aims to streamline waste sorting for better environmental sustainability.

Key Goals:
- Automate waste classification.
- Assist in efficient waste segregation.
- Reduce environmental pollution.

---

## 🌟 Features

✅ **Image-Based Waste Classification** – Predicts the waste category from uploaded images.  
✅ **User-Friendly Web App** – Built using Streamlit for easy access and use.  
✅ **Fast & Accurate Predictions** – Uses a trained deep learning model.  
✅ **Supports Multiple Categories** – Distinguishes between recyclable, organic, and non-recyclable waste.  

---

## 🎥 Demo

**Live Application:** [Waste Classifier Web App](Adding soon)  
![Screenshot 2025-03-24 202852](https://github.com/user-attachments/assets/88dd7b05-1774-4e0f-af9c-dd465129838b)
![Screenshot 2025-03-24 202929](https://github.com/user-attachments/assets/493bb74e-8172-4d88-b2ec-0123d2596cb5)

---

## 🔧 Installation

Follow these steps to set up the project on your local system:

### 1️⃣ Clone the Repository

git clone https://github.com/yashdubeyy/Green_Skill_Project.git
cd Green_Skill_Project

2️⃣ Set Up a Virtual Environment (Optional)

python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

3️⃣ Install Required Dependencies
pip install -r requirements.txt

🚀 Usage
1️⃣ Navigate to the Application Directory
cd streamlit_app

2️⃣ Run the Streamlit App
streamlit run app.py

3️⃣ Interact with the Web Interface
Upload an image of waste material.

Get an instant classification result.

Use the prediction to properly dispose of the waste.

🏗 Project Structure
Green_Skill_Project/
├── .devcontainer/        # Development container configuration
├── notebooks/            # Jupyter notebooks for model training
├── src/                  # Model training and evaluation scripts
├── streamlit_app/        # Streamlit web application
│   ├── app.py            # Main application script
│   ├── components/       # UI components
│   ├── static/           # Static files (e.g., images, CSS)
│   ├── utils/            # Helper functions
├── requirements.txt      # Python dependencies
├── LICENSE               # Project license
└── README.md             # Documentation
🛠 Technologies Used
Python – Main programming language.

TensorFlow / Keras – Deep learning framework for training the model.

Streamlit – Web application framework for interactive UI.

Jupyter Notebook – Used for model experimentation and training.

🤝 Contributing
💡 Want to contribute? Follow these steps:
Fork the Repository

Click the "Fork" button on GitHub.

Clone Your Fork

git clone https://github.com/your-username/Green_Skill_Project.git
cd Green_Skill_Project
Create a New Branch


git checkout -b feature/your-feature-name
Make Your Changes & Commit


git add .
git commit -m "Add: Your description of the changes"
Push Your Changes


git push origin feature/your-feature-name
Create a Pull Request

Go to the original repository on GitHub.

Click on "New Pull Request".

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

🎗 Acknowledgements
🙏 Special thanks to:

Dataset Providers – For making the dataset publicly available.

Open-Source Community – For contributing tools and libraries.

Contributors – For their valuable inputs and improvements.

