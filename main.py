from flask import Flask, request, jsonify
import pandas as pd
import category_encoders as ce
import joblib
from openai import OpenAI

# Create Flask app
app = Flask(__name__)

client = OpenAI(api_key="YOUR OPENAI API KEY HERE")  # Replace with your actual OpenAI API key

# Load pre-trained model, encoders, and scalers (obtained from RandomForestClassifier.ipynb)

random_forest = joblib.load('models/obesity_prediction_model.pkl')# Load the trained RandomForest model

encoder = joblib.load('models/numerical_encoder.pkl') # Load the trained numerical encoder

scaler = joblib.load("models/scaler.pkl")  # Load the trained scaler

ordinances = joblib.load("models/ordinal_encoder.pkl")  # Load the trained ordinal encoder
# Define prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the POST request
    user_data = request.get_json()

    if 'NObeyesdad' not in user_data:
        user_data['NObeyesdad'] = 'Insufficient_Weight'  # Default value if not provided, ensures all data is provided
        
        
    # Convert the user data into a pandas DataFrame
    df = pd.DataFrame([user_data])

    # Apply the same preprocessing steps as the training data
    # Encoding categorical data
    df_with_ohe = encoder.transform(df)
    
    encoded_data  = ordinances.transform(df_with_ohe)
    # Apply scaling to the features (except the label if it's encoded)
    features_scaled = scaler.transform(encoded_data.iloc[:, :-1])  # Exclude the target column for scaling
    
    # Use the model to predict the obesity level
    prediction = random_forest.predict(features_scaled)

    # Map prediction to obesity level (example: prediction categories can be changed)
    obesity_level = map_prediction_to_level(prediction[0])

    # Generate personalized advice (this could be based on the input or predefined advice)
    suggestions = generate_advice(obesity_level)

    # Return prediction and suggestions as JSON
    return jsonify({
        'obesity_level': obesity_level,
        'suggestions': suggestions
    })

# Helper function to map the model's prediction to a human-readable level
def map_prediction_to_level(prediction):
    levels = {
        0: "Insufficient Weight",
        1: "Normal Weight",
        2: "Overweight Level I",
        3: "Overweight Level II",
        4: "Obesity Type I",
        5: "Obesity Type II",
        6: "Obesity Type III"
    }
    return levels.get(prediction, "Unknown")

# Helper function to generate personalized advice based on obesity level
def generate_advice(obesity_level):
    try:
        # Generate suggestions using OpenAI API
        prompt = f"Provide simple and practical health and lifestyle suggestions for someone classified as '{obesity_level}' in terms of obesity."
        
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",  # Use the correct GPT-4 model (ensure you're using the correct model ID)
            messages=[
                {"role": "system", "content": "You are a healthcare professional in nutrition and exercise."},
                {"role": "user", "content": prompt}
            ]
        )
        return  completion.choices[0].message.content # Access the message content from the response
    except Exception as e:
        return f"Error generating suggestions: {str(e)}"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
