import streamlit as st
import plotly.express as px
import pandas as pd
from urllib.error import URLError
import plotly.graph_objects as go
import model
import time

from functions import *



toc = Toc()


        
sidebar(toc)



toc.title('Cardio Care')

st.markdown("Heart disease is the leading cause of death and \
    a major cause of disability in the United States. \
        About **<font color='red'>600,000 Americans</font>** die of heart disease annually. \
            This represents almost **<font color='red'>25% of all U.S. deaths</font>**. \
                To raise awareness of this disease, February \
                    has been recognized as “American Heart Month” since 1963.",unsafe_allow_html=True)


# audio('audio/speech_1.mp3')
toc.subheader("Top 7 Causes of Deaths in US")


death_causes_line_plot()


toc.subheader("Effect of Features")
st.markdown("**<font color='red'>Age is the most critical factor</font>** in getting heart disease. \
    Much more crucial than the second most important factor Diabetic. \
        As we can see in the previous chart, after **<font color='red'>age 60</font>** the counts of getting heart \
            disease is skyrocketing. Hence, it is recommended to do medical checkups after 60. \
                Stroke and DiffWalking are also crucial factors as they can give you four to six \
                    times higher risks.",unsafe_allow_html=True)

audio('audio/speech_2.mp3')



chi_square_bar_plot()
toc.subheader("Explore Contributing Features")


dynamic_bar_plot()


toc.subheader("Predict your Heart Disease Risk")

st.markdown("The heart disease risk can be predicted with the help \
of machine learning with great accuracy. Our model predict the heart risk probability for the \
patient. Recommended actions are also provided.")




create_form()

st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')


toc.subheader("How our model works")



model_explanation()
    

toc.generate()