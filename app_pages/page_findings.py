import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def page_findings_body():
    st.write("### Findings")
    st.write("This page shows how car attributes correlate with selling price.")
    
    # Load dataset
    df = pd.read_csv('../datasets/cleaned_car_data.csv')
    
    # Correlation heatmap
    st.image('../outputs/correlation_heatmap.png', caption='Correlation Heatmap')
    st.write("**Interpretation**: Present Price has a strong positive correlation with Selling Price.")
    
    # Scatter plot
    st.image('../outputs/present_vs_selling_price.png', caption='Present Price vs Selling Price')
    st.write("**Interpretation**: Higher present prices are associated with higher selling prices.")
    
    # Box plots
    st.image('../outputs/fuel_type_vs_selling_price.png', caption='Fuel Type vs Selling Price')
    st.write("**Interpretation**: Diesel cars tend to have higher selling prices than petrol cars.")
    
    st.image('../outputs/transmission_vs_selling_price.png', caption='Transmission vs Selling Price')
    st.write("**Interpretation**: Automatic cars have higher selling prices than manual cars.")