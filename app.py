import streamlit as st 
import pandas as pd

# Parameterized file path
DATA_PATH = 'datasets/car_dataset.csv'

st.title('🚗 Car Price Prediction')

st.markdown('## 📥 Load Original Dataset')
df = pd.read_csv(DATA_PATH)
st.success(f'✅ Loaded dataset with shape: {df.shape}')

# Display with gradient background on numeric columns
st.dataframe(df.style.background_gradient(cmap='BuGn'), use_container_width=True)

st.divider()

st.markdown('## 🧹 Clean Data')
df = df.dropna().reset_index(drop=True)
st.info(f'📏 Data shape after cleaning: {df.shape}')
st.dataframe(df.style.background_gradient(cmap='YlOrBr'), use_container_width=True)
