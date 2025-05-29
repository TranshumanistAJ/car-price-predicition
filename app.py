import streamlit as st
from app_pages.page_project_summary import page_project_summary_body
from app_pages.page_findings import page_findings_body
from app_pages.page_prediction_interface import page_prediction_interface_body
from app_pages.page_hypothesis_validation import page_hypothesis_validation_body
from app_pages.page_ml_metrics import page_ml_metrics_body

# Set page configuration
st.set_page_config(page_title="Car Price Prediction", layout="wide")

# Main navigation menu
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Project Summary",
    "Findings",
    "Prediction Interface",
    "Hypothesis and Validation",
    "ML Metrics"
])

# Page routing
if page == "Project Summary":
    page_project_summary_body()
elif page == "Findings":
    page_findings_body()
elif page == "Prediction Interface":
    page_prediction_interface_body()
elif page == "Hypothesis and Validation":
    page_hypothesis_validation_body()
elif page == "ML Metrics":
    page_ml_metrics_body()