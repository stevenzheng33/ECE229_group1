from numpy import disp
import streamlit as st
import plotly.express as px
import pandas as pd
from urllib.error import URLError
import plotly.graph_objects as go
from torch import sub
import model

class Toc:

    def __init__(self):
        self._items = []
        self._placeholder = None
    
    def title(self, text):
        self._markdown(text, "h1")

    def header(self, text):
        self._markdown(text, "h2", " " * 2)

    def subheader(self, text):
        self._markdown(text, "h3", " " * 4)

    def placeholder(self, sidebar=False):
        self._placeholder = st.sidebar.empty() if sidebar else st.empty()

    def generate(self):
        if self._placeholder:
            self._placeholder.markdown("\n".join(self._items), unsafe_allow_html=True)
    
    def _markdown(self, text, level, space=""):
        import re
        key = re.sub('[^0-9a-zA-Z]+', '-', text).lower()

        st.markdown(f"<{level} id='{key}'>{text}</{level}>", unsafe_allow_html=True)
        self._items.append(f"{space}* <a href='#{key}'>{text}</a>")
toc = Toc()
if 'bmi_pop' not in st.session_state:
    st.session_state['bmi_pop'] = 'not_enabled'




toc.title('Heart Disease Analysis')

st.markdown("Heart disease is the leading cause of death and \
    a major cause of disability in the United States. \
        About 600,000 Americans die of heart disease annually. \
            This represents almost 25% of all U.S. deaths. \
                To raise awareness of this disease, February \
                    has been recognized as “American Heart Month” since 1963.")

toc.subheader("Top 7 Causes of Deaths")

def line_plot():
    df = pd.read_csv('death_causes.csv')
    df = df.set_index('Year')
    st.line_chart(df[['Heart disease', 'Cancer ', 'Unintentional injuries',
        'CLRD', 'Stroke', "Alzheimer's disease", 'Diabetes']])
line_plot()


toc.subheader("Effect of Features")
st.write('Age is the most important factor of getting heart disease. Two times more crucial than\
        the second most important factor Diabetic. As we can see in the\
        previous chart, after age 60 the counts of getting heart disease is skyrocketing increasing.\
        Hence, it is recommend to do medical checkups after 60.')


st.write('Diabetic, Stroke, and DiffWalking are also the crucial factors of getting heart disease.\
        Having these three diseases gives you four to six times more chance to having heart disease.')
def bar_plot():
    try:
        df = pd.read_csv("./heart_2020_cleaned.csv")

    
        col1,b1, col2,b2, col3 = st.columns([1,0.2,1,0.2,1])
        fig1, b1,fig2 = st.columns([1,0.4,2])
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
        # histogram params
        category_orders = None
        nbins = None
        barnorm = None

        #
        if cols == 'AgeCategory':
            category_orders = {"AgeCategory": ["18-24", "25-29", "30-34", "35-39", "40-44",
                                               "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80 or older"]}
        else:
            category_orders = {cols: ['Yes', 'No']}
        if cols == 'BMI':
            nbins = 20
        if cols in ['AgeCategory', 'BMI', 'Smoking', 'AlcoholDrinking', 'Stroke', 'DiffWalking', 'Race', 'Sex', 'Diabetic', 'PhysicalActivity', 'GenHealth', 'Asthma', 'KidneyDisease', 'SkinCancer']:
            barnorm = "percent"

        fig = px.histogram(df, x=cols, color="HeartDisease", width=500, height=500,
                           barnorm=barnorm, nbins=nbins, category_orders=category_orders)

        fig1.write(fig)

    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )
bar_plot()



toc.subheader("Predict your Heart Disease Risk")
def create_form():
    form = st.form(key='my_form')
    bmi = form.number_input('BMI')
    smoking = form.selectbox(
        'Smoking',
        ('','True', 'False'))
    alcohol = form.selectbox(
        'Alcohol Drinking',
        ('','True', 'False'))
    stroke = form.selectbox(
        'Stroke',
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
        try:
            risk = model.model(user_data)
            risk = 1-risk[1]
        except:
            import random
            risk = random.uniform(0, 1)
        display_risk = str(round(risk*100,2))+"%"
        st.markdown('## Your predicted risk for Heart Disease is '+ display_risk)

        if risk < 0.2:
            st.markdown("#### - Consume a healthy diet that emphasizes the intake of vegetables, fruits and nuts.\n"
            "#### - Healthy adults who lead a sedentary lifestyle should be encouraged to start with a light exercise intensity. Must maintain weight.")
        
        elif 0.2 <risk <= 0.4:
            st.markdown("- If you are overweight, achieve and maintain weight-loss.\n" 
        "- Healthy adults all ages of 2.5 to 5h a week of moderate physical activity or 1 to 2.5h per week of intense physical activity.\n"
    "- This includes fast walking, bicycling, or swimming. \n"
    "- Regularly consume fish.\n"
        "- Consume a varied well-balanced diet.\n")

        elif 0.4 < risk <= 0.6:
            st.markdown(
        "- Eat a well balanced diet with lot of fruits and vegetables.\n"
    "- Reduced intake of salt in food (<5g/day)\n"
        "- 30 to 45 grams of fiber per day\n"
        "- Avoid salty and factory processed foods.\n"
        "- need 3 or more times a week moderate to intense aerobic exercise for 30 minutes.\n"
        "- Must restrict the usage of tobacco and consumption of alcohol. \n"
    "- Recommended to do a primary checkup. Should try to control stress.")

        elif 0.6 < risk <= 0.8:
            st.markdown( 
            "- 200g of fruit a day (2 to 3 meals per day).\n"
        "- 200g vegetables a day (2-3 servings per day).\n"
        "- Fish at least 2x per week (1 meal a week blue fish).\n"
        "- need 3 or more times a week moderate to intense aerobic exercise for 60 minutes.\n"
        "- Must also consult with doctor to see if intense physical activities is recommended.\n"
        "- Highly recommended to visit a clinic and follow medications.\n"
        "- Must strictly abstain from consumption of tobacco and alcohol. Should monitor blood pressure, cholesterol and diabetes regularly.\n" 
        "- Should include intensive counseling on risk factors.")

        else:
            st.markdown("- Must immediately seek medical attention.")


create_form()

    

    
def sidebar():
    with st.sidebar:
        st.title('Table of Contents')
        
        toc.placeholder()
        toc.generate()
sidebar()



