<<<<<<< HEAD
# AI-Powered Crop Recommendation System

An intelligent crop recommendation system that leverages a Random Forest machine learning model to predict the optimal crop to grow based on soil and environmental factors. The model is deployed as a user-friendly web application using the Flask framework.

---

## 📝 Project Overview

This project aims to assist farmers and agricultural professionals in making informed decisions about crop selection. By inputting key environmental parameters such as soil nutrient levels (Nitrogen, Phosphorus, Potassium), temperature, humidity, pH, and rainfall, the system's machine learning model provides an instantaneous recommendation for the most suitable crop, thereby helping to maximize yield and sustainability.

---

## 📊 Dataset

This project uses the [Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset) from Kaggle. This dataset includes 2200 data points on various crops under different environmental conditions.

The features include:
- `N`: Ratio of Nitrogen content in soil
- `P`: Ratio of Phosphorus content in soil
- `K`: Ratio of Potassium content in soil
- `temperature`: Temperature in degrees Celsius
- `humidity`: Relative humidity in %
- `ph`: pH value of the soil
- `rainfall`: Rainfall in mm
- `label`: The target crop

---

## ✨ Features

- **Intuitive Web Interface:** A clean and simple UI for users to input environmental data.
- **Real-time Predictions:** Get instant crop recommendations powered by a high-accuracy machine learning model.
- **Data-Driven Insights:** Based on a comprehensive dataset of agricultural conditions.
- **Scalable Backend:** Built with Flask, allowing for easy expansion and integration.

---

## 💻 Technology Stack

- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn, Pandas, NumPy
- **Frontend:** HTML, CSS, JavaScript

---

## 📸 Screenshots

#### **Web Application UI**
![Application UI](https://github.com/Vasu-uu/Crop-Recommendation-System/raw/main/Screenshots/ui.PNG)

#### **Sample Output**
![Sample Output](https://github.com/Vasu-uu/Crop-Recommendation-System/raw/main/Screenshots/s1.PNG)

---

## How to Run the Project Locally

Follow these steps to set up and run the project on your local machine:  

### 1️⃣ Clone the Repository
```bash
git https://github.com/Vasu-uu/Crop-Recommendation-System.git
cd Crop-Recommendation-System
```

### 2️⃣ Create and Activate a Virtual Environment

**For macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**For Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask Application
```bash
python app.py
```

### 5️⃣ Access the Application
Open your browser and go to:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

You should now see the application running and ready for predictions.

---

## Author

**Vasudev V**  
[GitHub - Vasu-uu](https://github.com/Vasu-uu)
=======
# Crop-Recommendation-System
It is a Machine Learning based Project
An AI-powered machine learning application that suggests the most suitable crop to grow based on soil and weather parameters.


This project uses a *Random Forest Classifier* to recommend crops by analyzing:
- Nitrogen (N) content in soil
- Phosphorus (P) content in soil
- Potassium (K) content in soil
- Temperature (°C)
- Humidity (%)
- pH level of soil
- Rainfall (mm)

Built using:
- Python
- Flask (for the web interface)
- Scikit-learn (for ML model)
- Pandas & NumPy (for data handling)

---

## 🚀 Features
- Simple and user-friendly web interface
- Fast and accurate crop predictions
- Easy to deploy locally or on the cloud
- Trained on agricultural dataset for multiple crop types
>>>>>>> 55c030484214c2e3e0a3859b76f2fe222f73183c
