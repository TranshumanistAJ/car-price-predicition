import streamlit as st
import pandas as pd

@st.cache_data
def load_data(path='datasets/car_dataset.csv'):
    df = pd.read_csv(path)
    return df.dropna().reset_index(drop=True)

def app():
    st.header("📜 Summary Scroll")
    df = load_data()
    
    st.success(f'✅ Dataset Loaded: {df.shape[0]} rows, {df.shape[1]} columns')
    
    with st.expander("🔍 Peek into the Data Scroll"):
        st.dataframe(df.head().style.background_gradient(cmap='BuGn'), use_container_width=True)

    st.markdown("### 🧾 Data Types")
    st.dataframe(df.dtypes.astype(str), use_container_width=True)

    st.markdown("### 📐 Descriptive Stats")
    st.dataframe(df.describe(), use_container_width=True)
