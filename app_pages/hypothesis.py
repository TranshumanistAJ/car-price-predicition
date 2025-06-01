import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data(path='datasets/car_dataset.csv'):
    df = pd.read_csv(path)
    return df.dropna().reset_index(drop=True)

def describe_feature(col, dtype):
    if dtype == 'object':
        return f"📊 **{col}** is a categorical feature. We'll explore how different categories affect the selling price."
    else:
        return f"📈 **{col}** is a numerical feature. We'll check its distribution and possible influence on selling price."

def app():
    st.header("🧪 Hypothesis Forge")
    df = load_data()

    st.markdown("🔍 **Form and test your theories about how different features influence car prices.**")

    num_cols = df.select_dtypes(include='number').columns.tolist()
    cat_cols = df.select_dtypes(include='object').columns.tolist()

    selected = st.selectbox("🧠 Choose a feature to explore:", num_cols + cat_cols)

    # Display dynamic description
    col_type = df[selected].dtype
    st.markdown(describe_feature(selected, col_type))

    # Plot based on type
    if selected in num_cols:
        # Distribution of numerical feature
        fig = px.histogram(df, x=selected, nbins=30, marginal='box', color_discrete_sequence=['indianred'])
        fig.update_layout(
            title=f"Distribution of {selected}",
            xaxis_title=selected,
            yaxis_title="Count",
            bargap=0.05
        )
    else:
        # Boxplot of categorical feature vs selling price
        fig = px.box(df, x=selected, y='selling_price', color=selected)
        fig.update_layout(
            title=f"Selling Price by {selected}",
            xaxis_title=selected,
            yaxis_title="Selling Price",
            xaxis_tickangle=-45
        )

    st.plotly_chart(fig, use_container_width=True)
