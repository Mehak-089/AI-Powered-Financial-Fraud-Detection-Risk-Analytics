import streamlit as st
import pandas as pd
import pickle  # Load ML model

# Load your trained fraud detection model
with open('fraud_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# UI Title
st.title("🚀 AI-Powered Financial Fraud Detection")
st.write("Enter transaction details to check fraud risk.")

# User Input Fields
amount = st.number_input("Transaction Amount ($)", min_value=0.01, format="%.2f")
time = st.slider("Transaction Time (24-hour format)", 0, 23)
device = st.selectbox("Device Type", ["Mobile", "Desktop", "Tablet"])
location = st.text_input("Transaction Location")

# Convert inputs to DataFrame for prediction
input_data = pd.DataFrame({
    'Amount': [amount],
    'Time': [time],
    'Device': [1 if device == "Mobile" else 2 if device == "Desktop" else 3],
    'Location_Hash': [hash(location) % 1000]  # Simplified encoding
})

# Predict fraud status
if st.button("Check Fraud Risk"):
    prediction = model.predict(input_data)
    fraud_probability = model.predict_proba(input_data)[:, 1][0]
    
    if prediction[0] == 1:
        st.error(f"⚠️ High Fraud Risk! (Probability: {fraud_probability:.2f})")
    else:
        st.success(f"✅ Safe Transaction (Probability: {fraud_probability:.2f})")

# Embed Tableau Dashboard
st.markdown("### 📊 Fraud Analytics Dashboard")
st.markdown("[View Full Dashboard](https://public.tableau.com/views/AI-PoweredFinancialFraudDetectionRiskDashboard/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)")
