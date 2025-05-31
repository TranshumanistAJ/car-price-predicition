import streamlit as st 
import pandas as pd


st.title('Car Price Prediction')

st.markdown('### Load original Dataset')
df = pd.read_csv('datasets/car_dataset.csv')

st.dataframe(df.head(5))


st.divider()


st.markdown('### Clean Data')
df = df.dropna().reset_index(drop = True)
st.dataframe(df)


