import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data(path='datasets/car_dataset.csv'):
    df = pd.read_csv(path)
    return df.dropna().reset_index(drop=True)

def app():
    st.header("🧪 Hypothesis Forge")
    df = load_data()

    st.markdown("Crafting theories about how each feature may influence car prices.")

    num_cols = df.select_dtypes(exclude='object').columns.tolist()
    cat_cols = df.select_dtypes(include='object').columns.tolist()

    selected = st.selectbox("🔍 Choose Feature to Test", num_cols + cat_cols)

    if selected in num_cols:
        fig = sns.histplot(data=df, x=selected, kde=True)
        st.pyplot(fig.figure)
    else:
        fig = sns.boxplot(data=df, x=selected, y='selling_price')
        plt.xticks(rotation=45)
        st.pyplot(fig.figure)
