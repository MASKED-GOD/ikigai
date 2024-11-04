from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the model
model = joblib.load('ikigai_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get the JSON data sent from the frontend

    # Ensure that the required fields are present in the data
    required_fields = ['motivation', 'skill', 'environment', 'impact', 'known_for']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    # Prepare the data for prediction
    input_data = {
        'motivation': data['motivation'],
        'skill': data['skill'],
        'environment': data['environment'],
        'impact': data['impact'],
        'known_for': data['known_for']
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])

    # Handle categorical data (one-hot encoding)
    input_encoded = pd.get_dummies(input_df)

    # Ensure it matches the model's expected input
    model_features = model.feature_names_in_  # Get the feature names used during training
    for feature in model_features:
        if feature not in input_encoded:
            input_encoded[feature] = 0  # Add missing features with value 0
    input_encoded = input_encoded[model_features]  # Reorder to match model

    # Make prediction
    prediction = model.predict(input_encoded)

    # Return the prediction
    return jsonify({'ikigai': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
