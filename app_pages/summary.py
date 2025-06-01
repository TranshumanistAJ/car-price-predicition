import streamlit as st
import pandas as pd

@st.cache_data
def load_data(path='datasets/car_dataset.csv'):
    df = pd.read_csv(path)
    return df.dropna().reset_index(drop=True)

def generate_column_summary(df):
    column_info = {
        "name": "The full name of the car (brand and model).",
        "year": "Year of manufacture — newer cars typically cost more.",
        "selling_price": "Target variable — the car's resale value.",
        "km_driven": "Total distance the car has been driven (in kilometers).",
        "fuel": "Type of fuel used (e.g., Petrol, Diesel, CNG, LPG, Electric).",
        "seller_type": "Who is selling the car — Individual, Dealer, or Trustmark Dealer.",
        "transmission": "Gear system — Manual or Automatic.",
        "owner": "How many previous owners the car has had.",
        "mileage(km/ltr/kg)": "Fuel efficiency — distance per unit of fuel.",
        "engine": "Engine capacity in cc — affects power and performance.",
        "max_power": "Maximum power output of the engine.",
        "seats": "Number of seats in the car."
    }

    rows = []
    for col in df.columns:
        dtype = df[col].dtype
        desc = column_info.get(col, "No description available.")
        rows.append({
            "Column": col,
            "Data Type": str(dtype),
            "Description": desc
        })

    return pd.DataFrame(rows)

def app():
    st.header("📜 Summary Scroll")
    st.markdown('''
    <div style="text-align: center; padding: 1rem 2rem; border-radius: 10px;">
        <h3>🔮 Project Overview</h3>
        <p style="font-size: 16px; line-height: 1.6;">
            This Streamlit project is a <strong>fantasy-themed car price analysis and prediction app</strong>.<br>
            It allows users to explore and understand a used car dataset through <strong>interactive summaries</strong>, 
            <strong>visual correlations</strong>, and <strong>descriptive statistics</strong>.<br>
            The app includes <strong>dynamic feature explanations</strong> for beginners, and an interactive 
            <strong>Plotly-based correlation heatmap</strong> to explore feature relationships.<br>
            Users can select which numerical columns to analyze, making it adaptable and user-friendly.<br>
            The goal is to build an <strong>engaging, data-driven interface</strong> for car price prediction and exploration.
        </p>
    </div>
    ''', unsafe_allow_html=True)
    df = load_data()
    
    st.success(f'✅ Dataset Loaded: {df.shape[0]} rows, {df.shape[1]} columns')

    st.dataframe(df.head().style.background_gradient(cmap='BuGn'), use_container_width=True)

    st.markdown("### 🧾 Data Types")
    st.dataframe(df.dtypes.astype(str), use_container_width=True)

    st.markdown("### 📐 Descriptive Stats")
    st.dataframe(df.describe(), use_container_width=True)

    st.markdown("### 🔎 Column-by-Column Guide")
    col_summary_df = generate_column_summary(df)
    st.dataframe(col_summary_df, use_container_width=True)
