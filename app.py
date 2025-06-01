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


# Define features and target
X = df.drop(columns=['selling_price'])
y = df['selling_price']

# Show Features and Target column names
st.markdown('## 🧾 Features and Target')

st.write('### Features (X)')
st.write(X.columns.tolist())
st.write('### Target (y)')
st.write(f'{y.name} is column name')

st.divider()

# select numerical and categorical data
# List of categorical and numerical columns
categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
numerical_cols = X.select_dtypes(exclude=['object']).columns.tolist()


# preprocess to adjust the data according to ML model
preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
], remainder='passthrough')  # Pass through numerical columns

# make structure of model
model = Pipeline([
    ('preprocess', preprocessor),
    ('regressor', RandomForestRegressor())
])

# Train/test split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

