import streamlit as st
import pandas as pd
import scipy.stats as stats

def page_hypothesis_validation_body():
    st.write("### Hypothesis and Validation")
    st.write("**Hypothesis 1**: Cars with lower age and fewer kilometers driven have higher selling prices.")
    st.write("**Validation**: Correlation analysis shows negative correlations between Age/Kms_Driven and Selling Price.")
    
    st.write("**Hypothesis 2**: Diesel cars have higher selling prices than petrol cars.")
    st.write("**Validation**: Box plot analysis confirms diesel cars have higher median selling prices.")
    
    # T-test for statistical validation
    df = pd.read_csv('../datasets/cleaned_car_data.csv')
    diesel_prices = df[df['Fuel_Type'] == 'Diesel']['Selling_Price(lacs)']
    petrol_prices = df[df['Fuel_Type'] == 'Petrol']['Selling_Price(lacs)']
    t_stat, p_value = stats.ttest_ind(diesel_prices, petrol_prices)
    st.write(f"T-test p-value: {p_value:.4f} (significant if < 0.05, confirming hypothesis)")
    
    st.write("**Hypothesis 3**: Manual transmission cars have lower selling prices than automatic.")
    st.write("**Validation**: Box plot analysis shows automatic cars have higher median selling prices.")