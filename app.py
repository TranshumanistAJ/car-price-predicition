import streamlit as st 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor


# Parameterized file path
DATA_PATH = 'datasets/car_dataset.csv'

st.title('🚗 Car Price Prediction')

st.markdown('## 📥 Load Original Dataset')
df = pd.read_csv(DATA_PATH)
st.success(f'✅ Loaded dataset with shape: {df.shape}')

# Display with gradient background on numeric columns
original_head = df.head()
st.dataframe(original_head.style.background_gradient(cmap='BuGn'), use_container_width=True)

st.divider()

st.markdown('## 🧹 Clean Data')
df = df.dropna().reset_index(drop=True)
st.info(f'📏 Data shape after cleaning: {df.shape}')
cleaned_head = df.head()
st.dataframe(cleaned_head.style.background_gradient(cmap='YlOrBr'), use_container_width=True)
