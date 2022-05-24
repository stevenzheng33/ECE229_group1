import streamlit as st
import plotly.express as px
import pandas as pd
from urllib.error import URLError
import plotly.graph_objects as go

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



df = pd.read_csv('death_causes.csv')
df = df.set_index('Year')
# st.write("This is a dataframe displaying cause of deaths")
# st.write(df)
# st.bar_chart(df['Heart disease'])

def plot_distribution(col):
    df2 = pd.read_csv("heart_2020_cleaned.csv")
def radar_chart(df):
    theta = ['AlcoholDrinking', 'MentalHealth']
    fig = px.line_polar(df, r=[1, 2], theta=theta, line_close=True)
    st.write(fig)


try:
    df = pd.read_csv("./heart_2020_cleaned.csv")
    # df["HeartDisease"].replace({'No':0, 'Yes':1}, inplace=True)
    # radar_chart(df)

    
    col1,b1, col2,b2, col3 = st.columns([1,0.2,1,0.2,1])
    fig1, b1,fig2 = st.columns([1,0.4,2])
    #print(len(df["HeartDisease"] == 0))
    #print(len(df["HeartDisease"] == 1))
    metrics =['Smoking',
    'AlcoholDrinking',
    'Stroke',
    'DiffWalking',
    'Sex',
    'AgeCategory',
    'Race',
    'Diabetic',
    'PhysicalActivity',
    'GenHealth',
    'Asthma',
    'KidneyDisease',
    'SkinCancer',
    'BMI']
    
    cols = col1.selectbox('Factor metric to view', metrics)

    fig = px.histogram(df, x=cols, color="HeartDisease",width=500, height=500)

    fig1.write(fig)

    # cols1 = col2.selectbox('Metric1 to view for correlation', metrics)
    # cols2 = col3.selectbox('Metric2 to view for correlation', metrics)

    # fig_2 = px.scatter(df, x=cols1,y=cols2, color="HeartDisease",width=400, height=250)


    # fig2.write(fig_2)
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**

        Connection error: %s
    """
        % e.reason
    )



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



