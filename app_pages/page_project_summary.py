import streamlit as st

def page_project_summary_body():
    st.write("### Project Summary")
    st.write("""
    **Car Price Prediction** is a Streamlit-based Data App designed to predict car selling prices based on attributes such as Present Price, Kilometers Driven, Fuel Type, Seller Type, Transmission, Past Owners, and Age. The app provides data visualizations to analyze correlations and a prediction interface to estimate selling prices.
    
    #### Dataset Description
    - **Source**: [Kaggle Vehicle Dataset](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho)
    - **Attributes**:
      - **Car_Name**: Name of the car
      - **Selling_Price(lacs)**: Selling price in lacs
      - **Present_Price(lacs)**: Current market price in lacs
      - **Kms_Driven**: Kilometers driven
      - **Fuel_Type**: Petrol, Diesel, or CNG
      - **Seller_Type**: Dealer or Individual
      - **Transmission**: Manual or Automatic
      - **Past_Owners**: Number of previous owners
      - **Age**: Age of the car (derived from Year)
    
    #### Client Requirements
    - **BR1**: Conduct a study to understand how car attributes correlate with selling price.
    - **BR2**: Predict the selling price of a car based on its attributes.
    
    #### Project Goals
    - Deliver actionable insights through data visualizations (e.g., correlation heatmaps, scatter plots, box plots).
    - Build a machine learning model (Gradient Boosting Regressor) to predict car prices with an R² score ≥ 0.85.
    - Provide an interactive dashboard for stakeholders to input car attributes and receive price predictions.
    
    #### Target Audience
    - Car dealerships, individual sellers, and buyers looking to accurately price vehicles based on market trends.
    """)