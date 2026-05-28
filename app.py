from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import numpy as np
import pandas as pd
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

model_filename = 'model.pkl'
try:
    with open(model_filename, 'rb') as file:
        model = pickle.load(file)
    print("Model loaded successfully.")
except FileNotFoundError:
    print(f"Error: Model file '{model_filename}' not found. Please run the training script first.")
    model = None 

@app.route('/')
def home():
    """Renders the main page with the input form."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Receives input data from the form, makes a prediction using the loaded model,
    and returns the result as JSON.
    """
    if model is None:
        return jsonify({'error': 'Model not loaded. Please check server logs.'}), 500

    try:

        data = request.get_json()
        features = [
            float(data['N']),
            float(data['P']),
            float(data['K']),
            float(data['temperature']),
            float(data['humidity']),
            float(data['ph']),
            float(data['rainfall'])
        ]

        final_features = np.array(features).reshape(1, -1)

        prediction = model.predict(final_features)

        predicted_crop = prediction[0]

        return jsonify({'prediction': predicted_crop})

    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({'error': 'An error occurred during prediction. Please check your input.'}), 400


if __name__ == "__main__":
    # Dynamic port for deployment platforms (Render, Vercel, etc.)
    port = int(os.environ.get('PORT', 5000))
    
    # Set debug based on environment
    debug_mode = os.environ.get('FLASK_ENV', 'development') == 'development'
    
    app.run(host='0.0.0.0', port=port, debug=debug_mode)

