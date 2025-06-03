import streamlit as st  # Importing Streamlit for building the app interface
import pandas as pd  # Importing pandas for data manipulation

@st.cache_data  # Cache the data to avoid reloading on every run
def load_data(path='datasets/car_dataset.csv'):
    df = pd.read_csv(path)  # Read dataset from the given path
    return df.dropna().reset_index(drop=True)  # Remove missing values and reset index

def generate_column_summary(df):  # Function to create a summary of dataset columns
    column_info = {  # Dictionary mapping column names to their descriptions
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

    rows = []  # List to store summary rows
    for col in df.columns:  # Loop over each column in the dataset
        dtype = df[col].dtype  # Get the data type of the column
        desc = column_info.get(col, "No description available.")  # Get description or default message
        rows.append({  # Append column details as a dictionary
            "Column": col,
            "Data Type": str(dtype),
            "Description": desc
        })

    return pd.DataFrame(rows)  # Convert the list of dictionaries to a DataFrame

def app():
    st.markdown('''  # Render a styled HTML block for the project introduction
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
    df = load_data()  # Load the dataset
    
    st.success(f'✅ Dataset Loaded: {df.shape[0]} rows, {df.shape[1]} columns')  # Show success message with dataset shape

    st.dataframe(df.head().style.background_gradient(cmap='BuGn'), use_container_width=True)  # Show first few rows with styling

    st.markdown("### 🧾 Data Types")  # Section title for data types
    st.dataframe(df.dtypes.astype(str), use_container_width=True)  # Display data types of all columns

    st.markdown("### 📐 Descriptive Stats")  # Section title for descriptive statistics
    st.dataframe(df.describe(), use_container_width=True)  # Show summary stats of numerical columns

    st.markdown("### 🔎 Column-by-Column Guide")  # Section title for column descriptions
    col_summary_df = generate_column_summary(df)  # Generate column summary
    st.dataframe(col_summary_df, use_container_width=True)  # Display the column summary table
