import streamlit as st
import pandas as pd

st.title('Machine learning app')

st.info('this is a machine learning app')

with st.expander('Data'):
  st.write('**Raw Data**')
  df=pd.read_csv('https://raw.githubusercontent.com/aryahegde03-gif/a-machine-learning/refs/heads/master/customers-100.csv')
  df
