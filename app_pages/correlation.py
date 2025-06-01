import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data(path='datasets/car_dataset.csv'):
    df = pd.read_csv(path)
    return df.dropna().reset_index(drop=True)

def app():
    st.header("📊 Correlation Map")
    df = load_data()
    
    st.markdown("Visualizing magical connections between numerical features.")

    corr = df.select_dtypes(exclude='object').corr()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='crest', ax=ax)
    st.pyplot(fig)
