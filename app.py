import streamlit as st 
import pandas as pd


st.title('Car Price Prediction')

st.markdown('### Load Dataset')
df = pd.read_csv('datasets/car_dataset.csv')

st.dataframe(df)


st.divider()


st.markdown('### information')

