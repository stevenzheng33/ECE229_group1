import streamlit as st
import pandas as pd
st.title('Heart Disease Analysis')
df = pd.read_csv('death_causes.csv')
df = df.set_index('Year')
st.write("This is a dataframe displaying cause of deaths")
st.write(df)
st.bar_chart(df['Heart disease'])