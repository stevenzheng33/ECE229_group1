import streamlit as st
import pandas as pd

df = pd.read_csv('death_causes.csv')
df.set_index('Year')
st.write("Here's our first attempt at using data to create a table:")
st.write(df)
st.bar_chart(df[['Heart disease']])