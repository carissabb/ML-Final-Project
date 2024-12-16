import streamlit as st
import requests

# Backend URL (ensure this matches the Flask backend's URL)
backend_url = "http://127.0.0.1:5000/predict"


# Streamlit app title
st.title("Obesity Level Predictor & Lifestyle Advisor")

# Collect user input via Streamlit UI elements
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 10, 100)
height = st.number_input("Height (cm)", min_value=50, max_value=250)
weight = st.number_input("Weight (kg)", min_value=10, max_value=300)
family_history = st.selectbox("Family history of overweight?", ["Yes", "No"])
favc = st.selectbox("Do you eat high-calorie food frequently?", ["Yes", "No"])
fcvc = st.slider("Frequency of vegetable consumption (1-3)", 1, 3)
ncp = st.slider("Number of main meals (1-6)", 1, 6)
caec = st.selectbox("Do you eat food between meals?", ["No", "Sometimes", "Frequently", "Always"])
smoke = st.selectbox("Do you smoke?", ["Yes", "No"])
ch2o = st.slider("Daily water intake (liters)", 1, 5)
scc = st.selectbox("Do you monitor your calorie intake?", ["Yes", "No"])
faf = st.slider("Physical activity frequency (hours/week)", 0, 7)
tue = st.slider("Time using technology (hours/day)", 0, 24)
calc = st.selectbox("Consumption of alcohol", ["No", "Sometimes", "Frequently", "Always"])
mtrans = st.selectbox("Mode of transportation", ["Walking", "Bike", "Public", "Motorbike", "Car"])

# Prepare data for backend prediction
user_data = {
    "Gender": gender,
    "Age": age,
    "Height": height,
    "Weight": weight,
    "family_history_with_overweight": family_history,
    "FAVC": favc,
    "FCVC": fcvc,
    "NCP": ncp,
    "CAEC": caec,
    "SMOKE": smoke,
    "CH2O": ch2o,
    "SCC": scc,
    "FAF": faf,
    "TUE": tue,
    "CALC": calc,
    "MTRANS": mtrans
}

# Button to trigger prediction and advice generation
if st.button("Predict & Get Advice"):
    try:
        # Send user data to the Flask backend
        response = requests.post(backend_url, json=user_data)
        
        # Check the response from the backend
        if response.status_code == 200:
            result = response.json()
            st.success("Prediction successful!")
            st.write(f"**Obesity Level:** {result['obesity_level']}")
            st.write("**Suggestions for Improvement:**")
            st.write(result['suggestions'])
        elif response.status_code == 403:
            st.error("Access forbidden. Please check the backend permissions or CORS settings.")
        else:
            st.error(f"Unexpected error: {response.status_code}")
            st.write(response.text)  # Display error details for debugging
    except requests.exceptions.RequestException as e:
        st.error("Unable to connect to the backend. Please ensure the backend is running and accessible.")
        st.write(str(e))  # Display exception details for debugging