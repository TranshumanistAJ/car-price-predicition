import streamlit as st  # Importing Streamlit for building the app interface
import pandas as pd  # Importing pandas for data manipulation
import numpy as np  # Importing numpy for numerical operations
from sklearn.model_selection import train_test_split  # For splitting data into train and test sets
from sklearn.preprocessing import OneHotEncoder  # For encoding categorical variables
from sklearn.compose import ColumnTransformer  # To apply transformers to specific columns
from sklearn.pipeline import Pipeline  # For creating machine learning pipelines
from sklearn.ensemble import RandomForestRegressor  # Random Forest algorithm for regression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error  # Evaluation metrics
import plotly.express as px  # Plotly Express for visualizations

@st.cache_data  # Cache the data to prevent reloading every time
def load_data(path='datasets/car_dataset.csv'):
    df = pd.read_csv(path) # dataset is taken grom kaggle
    return df.dropna().reset_index(drop=True)  # Remove rows with missing values and reset index

@st.cache_resource  # Cache the pipeline creation
def get_pipeline(cat_cols):
    preprocessor = ColumnTransformer([
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols)  # One-hot encode categorical columns
    ], remainder='passthrough')  # Keep the rest of the columns unchanged

    model = Pipeline([  # Create a pipeline combining preprocessing and model
        ('preprocess', preprocessor),
        ('regressor', RandomForestRegressor(random_state=42))  # Use Random Forest as the regression model
    ])
    return model

def app():
    st.header("🎯 Prediction Portal")  # Main header of the app
    df = load_data()  # Load the dataset
    
    X = df.drop(columns=['selling_price'])  # Features (excluding the target variable)
    y = df['selling_price']  # Target variable
    
    cat_cols = X.select_dtypes(include='object').columns.tolist()  # List of categorical feature names
    num_cols = X.select_dtypes(exclude='object').columns.tolist()  # List of numerical feature names

    model = get_pipeline(cat_cols)  # Get the ML pipeline

    if 'model_trained' not in st.session_state:
        st.session_state.model_trained = False  # Track if the model has been trained

    if st.button("🚀 Train Model"):  # Button to train the model
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # Split data
        model.fit(X_train, y_train)  # Train the model

        y_pred = model.predict(X_test)  # Predict on test data
        r2 = r2_score(y_test, y_pred)  # R-squared score
        mae = mean_absolute_error(y_test, y_pred)  # Mean Absolute Error
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))  # Root Mean Squared Error

        st.session_state.update({  # Save the trained model and prediction results in session state
            'model_trained': True,
            'model': model,
            'X_test': X_test,
            'y_test': y_test,
            'y_pred': y_pred
        })

        st.success(f"✅ Trained! R²: {r2:.2f}, MAE: {mae:,.0f}, RMSE: {rmse:,.0f}")  # Display training success and metrics

    if st.session_state.model_trained:  # If model is trained, show prediction input UI
        st.subheader("🧾 Enter Features")  # Subheader for input section
        input_data = {}  # Dictionary to store user inputs

        cols = st.columns(len(cat_cols))  # Create columns for categorical inputs
        for i, col in enumerate(cat_cols):
            input_data[col] = cols[i].selectbox(col, sorted(df[col].unique()))  # Dropdown for each categorical feature

        cols = st.columns(len(num_cols))  # Create columns for numerical inputs
        for i, col in enumerate(num_cols):
            input_data[col] = cols[i].number_input(  # Numeric input with min, max, and mean values
                col, float(df[col].min()), float(df[col].max()), float(df[col].mean()))

        if st.button("🔮 Predict Price"):  # Button to trigger prediction
            input_df = pd.DataFrame([input_data])  # Convert input to DataFrame
            pred_price = st.session_state.model.predict(input_df)[0]  # Predict selling price
            st.success(f"💰 **Predicted Selling Price: $ {pred_price:,.0f}**")  # Display predicted price
    else:
        st.warning("⚠️ Train the model first.")  # Show warning if model is not trained yet
