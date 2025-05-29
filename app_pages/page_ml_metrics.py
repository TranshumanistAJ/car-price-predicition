import streamlit as st
import pandas as pd

def page_ml_metrics_body():
    st.write("### ML Metrics")
    st.write("The Gradient Boosting Regressor was trained with hyperparameter optimization.")
    st.write("**Performance**:")
    st.write("- Train R²: 0.95")
    st.write("- Test R²: 0.94")
    st.image('../outputs/actual_vs_predicted.png', caption='Actual vs Predicted Selling Price')
    st.write("**Conclusion**: The model meets the success criteria (R² ≥ 0.85).")