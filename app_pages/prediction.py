import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import plotly.express as px

@st.cache_data
def load_data(path='datasets/car_dataset.csv'):
    df = pd.read_csv(path) # dataset is taken grom kaggle
    return df.dropna().reset_index(drop=True)

@st.cache_resource
def get_pipeline(cat_cols):
    preprocessor = ColumnTransformer([
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols)
    ], remainder='passthrough')

    model = Pipeline([
        ('preprocess', preprocessor),
        ('regressor', RandomForestRegressor(random_state=42))
    ])
    return model

def app():
    st.header("🎯 Prediction Portal")
    df = load_data()
    
    X = df.drop(columns=['selling_price'])
    y = df['selling_price']
    
    cat_cols = X.select_dtypes(include='object').columns.tolist()
    num_cols = X.select_dtypes(exclude='object').columns.tolist()

    model = get_pipeline(cat_cols)

    if 'model_trained' not in st.session_state:
        st.session_state.model_trained = False

    if st.button("🚀 Train Model"):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))

        st.session_state.update({
            'model_trained': True,
            'model': model,
            'X_test': X_test,
            'y_test': y_test,
            'y_pred': y_pred
        })

        st.success(f"✅ Trained! R²: {r2:.2f}, MAE: {mae:,.0f}, RMSE: {rmse:,.0f}")

    if st.session_state.model_trained:
        st.subheader("🧾 Enter Features")
        input_data = {}

        cols = st.columns(len(cat_cols))
        for i, col in enumerate(cat_cols):
            input_data[col] = cols[i].selectbox(col, sorted(df[col].unique()))

        cols = st.columns(len(num_cols))
        for i, col in enumerate(num_cols):
            input_data[col] = cols[i].number_input(
                col, float(df[col].min()), float(df[col].max()), float(df[col].mean()))

        if st.button("🔮 Predict Price"):
            input_df = pd.DataFrame([input_data])
            pred_price = st.session_state.model.predict(input_df)[0]
            st.success(f"💰 **Predicted Selling Price: $ {pred_price:,.0f}**")
    else:
        st.warning("⚠️ Train the model first.")
