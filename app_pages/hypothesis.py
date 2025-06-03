import streamlit as st  # Importing Streamlit for web app interface
import pandas as pd  # Importing pandas for data handling
import plotly.express as px  # Importing Plotly Express for data visualization

@st.cache_data  # Caching the data loading function to avoid reloading on every run
def load_data(path='datasets/car_dataset.csv'):
    df = pd.read_csv(path)  # Read the dataset from the given path
    return df.dropna().reset_index(drop=True)  # Drop missing values and reset index

def describe_feature(col, dtype):
    if dtype == 'object':  # If the column is categorical
        return f"📊 **{col}** is a categorical feature. We'll explore how different categories affect the selling price."
    else:  # If the column is numerical
        return f"📈 **{col}** is a numerical feature. We'll check its distribution and possible influence on selling price."

def app():
    st.header("🧪 Hypothesis Forge")  # Main title of the app section
    df = load_data()  # Load the dataset

    st.markdown("🔍 **Form and test your theories about how different features influence car prices.**")  # Introductory text

    num_cols = df.select_dtypes(include='number').columns.tolist()  # Get list of numerical column names
    cat_cols = df.select_dtypes(include='object').columns.tolist()  # Get list of categorical column names

    selected = st.selectbox("🧠 Choose a feature to explore:", num_cols + cat_cols)  # Dropdown for feature selection

    # Display dynamic description
    col_type = df[selected].dtype  # Get the data type of the selected column
    st.markdown(describe_feature(selected, col_type))  # Show description based on column type

    # Plot based on type
    if selected in num_cols:
        # Distribution of numerical feature
        fig = px.histogram(df, x=selected, nbins=30, marginal='box', color_discrete_sequence=['indianred'])  # Histogram with boxplot
        fig.update_layout(
            title=f"Distribution of {selected}",  # Title of the plot
            xaxis_title=selected,  # X-axis label
            yaxis_title="Count",  # Y-axis label
            bargap=0.05  # Gap between bars
        )
    else:
        # Boxplot of categorical feature vs selling price
        fig = px.box(df, x=selected, y='selling_price', color=selected)  # Box plot comparing selling price
        fig.update_layout(
            title=f"Selling Price by {selected}",  # Title of the plot
            xaxis_title=selected,  # X-axis label
            yaxis_title="Selling Price",  # Y-axis label
            xaxis_tickangle=-45  # Rotate x-axis labels for better readability
        )

    st.plotly_chart(fig, use_container_width=True)  # Display the chart with full width
