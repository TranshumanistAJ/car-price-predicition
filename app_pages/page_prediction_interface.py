import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

def page_prediction_interface_body():
    st.write("### Prediction Interface")
    st.write("Input car attributes to predict the selling price.")
    
    # Load model and scaler
    model = joblib.load('../outputs/gradient_boosting.pkl')
    scaler = StandardScaler()
    df = pd.read_csv('../datasets/processed_car_data.csv')
    numerical_cols = ['Present_Price(lacs)', 'Kms_Driven', 'Past_Owners', 'Age']
    scaler.fit(df[numerical_cols])
    
    # Input widgets
    present_price = st.number_input("Present Price (lacs)", min_value=0.0, value=5.0)
    kms_driven = st.number_input("Kilometers Driven", min_value=0, value=30000)
    past_owners = st.number_input("Past Owners", min_value=0, value=0, step=1)
    age = st.number_input("Age (years)", min_value=0, value=5, step=1)
    fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'CNG'])
    seller_type = st.selectbox("Seller Type", ['Dealer', 'Individual'])
    transmission = st.selectbox("Transmission", ['Manual', 'Automatic'])
    
    # Prepare input data
    input_data = {
        'Present_Price(lacs)': [present_price],
        'Kms_Driven': [kms_driven],
        'Past_Owners': [past_owners],
        'Age': [age],
        'Fuel_Type_Diesel': [1 if fuel_type == 'Diesel' else 0],
        'Fuel_Type_Petrol': [1 if fuel_type == 'Petrol' else 0],
        'Seller_Type_Individual': [1 if seller_type == 'Individual' else 0],
        'Transmission_Manual': [1 if transmission == 'Manual' else 0]
    }
    input_df = pd.DataFrame(input_data)
    input_df[numerical_cols] = scaler.transform(input_df[numerical_cols])
    
    # Predict
    if st.button("Predict"):
        prediction = model.predict(input_df)[0]
        st.write(f"Predicted Selling Price: {prediction:.2f} lacs")