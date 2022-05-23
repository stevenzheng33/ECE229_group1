import streamlit as st
import pandas as pd

st.title('Heart Disease Analysis')
df = pd.read_csv('death_causes.csv')
df = df.set_index('Year')
st.write("Heart disease is the leading cause of death and \
    a major cause of disability in the United States. \
        About 600,000 Americans die of heart disease annually. \
            This represents almost 25% of all U.S. deaths. \
                To raise awareness of this disease, February \
                    has been recognized as “American Heart Month” since 1963.")

st.line_chart(df[['Heart disease', 'Cancer ', 'Unintentional injuries',
       'CLRD', 'Stroke', "Alzheimer's disease", 'Diabetes']])





m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #FF4B4B;
    height: 8em;
    width: 12em; 
}
</style>""", unsafe_allow_html=True)

b = st.button("CDC Heart Disease Information")

BMI = st.number_input('BMI')

smoking = st.selectbox(
     'Smoking',
     ('','True', 'False'))
alcohol_drinking = st.selectbox(
     'Alcohol Drinking',
     ('','True', 'False'))

stroke = st.selectbox(
     'stroke',
     ('','True', 'False'))
diff_walking = st.selectbox(
     'Difficult Walking',
     ('','True', 'False'))
sex = st.selectbox(
     'Gender',
     ('','Male', 'Female'))

age_category = st.number_input('Age')

race  = st.selectbox(
     'Race',
     ('','White', 'Black', 'Asian', 'American Indian/Alaskan Native',
       'Other', 'Hispanic'))

diabetic = st.selectbox(
     'Diabetic',
     ('','True', 'False'))

physical_activity = st.selectbox(
     'Physical Activity',
     ('','True', 'False'))

general_health = st.selectbox(
    'General Health',
    ('','Very good', 'Fair', 'Good', 'Poor', 'Excellent')
)
sleeptime = st.number_input('SleepTime (Hours)')

asthma = st.selectbox(
     'Asthma',
     ('','True', 'False'))

kidney_disease = st.selectbox(
     'Kidney Disease',
     ('','True', 'False'))

skin_cancer = st.selectbox(
    'Skin Cancer',
     ('','True', 'False'))



if st.button("Predict"):
    st.write("123")



