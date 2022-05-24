import streamlit as st
import plotly.express as px
import pandas as pd
from urllib.error import URLError
import plotly.graph_objects as go
import model
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



# m = st.markdown("""
# <style>
# div.stButton > button:first-child {
#     background-color: #FF4B4B;
#     height: 8em;
#     width: 12em; 
# }
# </style>""", unsafe_allow_html=True)

b = st.button("CDC Heart Disease Information")



form = st.form(key='my_form')
bmi = form.number_input('BMI')
smoking = form.selectbox(
     'Smoking',
     ('','True', 'False'))
alcohol = form.selectbox(
     'Alcohol Drinking',
     ('','True', 'False'))
stroke = form.selectbox(
     'stroke',
     ('','True', 'False'))
walking = form.selectbox(
     'Difficult Walking',
     ('','True', 'False'))
sex = form.selectbox(
     'Gender',
     ('','Male', 'Female'))

age = form.number_input('Age')

race = form.selectbox(
     'Race',
     ('','White', 'Black', 'Asian', 'American Indian/Alaskan Native',
       'Other', 'Hispanic'))

diabetic = form.selectbox(
     'Diabetic',
     ('','True', 'False'))

activity = form.selectbox(
     'Physical Activity',
     ('','True', 'False'))

health = form.selectbox(
    'General Health',
    ('','Very good', 'Fair', 'Good', 'Poor', 'Excellent')
)
sleep = form.number_input('SleepTime (Hours)')

asthma = form.selectbox(
     'Asthma',
     ('','True', 'False'))

kidney = form.selectbox(
     'Kidney Disease',
     ('','True', 'False'))

skin = form.selectbox(
    'Skin Cancer',
     ('','True', 'False'))
submit_button = form.form_submit_button(label='Submit')
if submit_button:
    user_data = {
                'HeartDisease'      :'Yes',
                'BMI'                :bmi,
                'Smoking'            :smoking,
                'AlcoholDrinking'    :alcohol,
                'Stroke'            :stroke,
                'DiffWalking'        :walking,
                'Sex'                :sex,
                'AgeCategory'        :model.age_tranform(age),
                'Race'                :race,
                'Diabetic'            :diabetic,
                'PhysicalActivity'    :activity,
                'GenHealth'            :health,
                'SleepTime'            :sleep,
                'Asthma'            :asthma,
                'KidneyDisease'        :kidney,
                'SkinCancer'        :skin,}

    risk = model.model(user_data)
    
    st.write(f'Your predicted risk for Heart Disease is {1-risk[1]}.')





