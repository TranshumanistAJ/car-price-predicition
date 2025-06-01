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
    st.markdown('''### ''')
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
