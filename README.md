# AI-Powered Crop Recommendation System

An intelligent crop recommendation system that leverages a Random Forest machine learning model to predict the optimal crop to grow based on soil and environmental factors. The model is deployed as a user-friendly web application using the Flask framework.

**Live Demo:** [https://crop-recommendation-4i0t.onrender.com](https://crop-recommendation-4i0t.onrender.com)

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
- **Cloud Deployed:** Hosted on Render for instant access.

---

## 💻 Technology Stack

- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn, Pandas, NumPy
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Render

---

## 📸 Screenshots

Screenshots are available in the `Screenshots/` directory of the repository.

---

## How to Run the Project Locally

Follow these steps to set up and run the project on your local machine:  

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/sinchana-Hegde1/crop_recommendation.git
cd crop_recommendation
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



You should now see the application running and ready for predictions.

---

## 🚀 Deployment

This project is deployed on **Render** and is live at: [https://crop-recommendation-4i0t.onrender.com](https://crop-recommendation-4i0t.onrender.com)

For deployment instructions, see [DEPLOYMENT.md](./DEPLOYMENT.md).

---

## Author

**Sinchana Hegde**  
[GitHub - sinchana-Hegde1](https://github.com/sinchana-Hegde1)  
[Repository - crop_recommendation](https://github.com/sinchana-Hegde1/crop_recommendation)
