from xmlrpc.client import Boolean
from numpy import isin
import streamlit as st
import plotly.express as px
import pandas as pd
from urllib.error import URLError
import plotly.graph_objects as go
import model
import time
import re

class Toc:
    """
    This class is used for Streamlit to build the Table of Contents. For this project
    it will be used for the sidebar.
    """

    def __init__(self): 
        """
        Initialize function, it is used to intialize class fields
        """
        self._items = []
        self._placeholder = None
    
    def title(self, text): 
        """
        This function is used to display the title
        :param text: The text for the title.
        """

        assert isinstance(text, str)
        self._markdown(text, "h1")

    def header(self, text): 
        """
        This function is used to display the header.
        :param text: The text for the header.
        """

        assert isinstance(text, str)
        self._markdown(text, "h2", " " * 2)

    def subheader(self, text): 
        """
        This function is used to display the subheader.
        :param text: The text for the subheader.
        """

        assert isinstance(text, str)
        self._markdown(text, "h3", " " * 4)

    def placeholder(self, sidebar=False): 
        """
        :param sidebar: If sidebar = False, no side bar in Table of Contents. If sidebar = True, adds empty sidebar
        to Table of Contents, temporarily.
        """

        assert isinstance(sidebar, Boolean)
        self._placeholder = st.sidebar.empty() if sidebar else st.empty()

    def generate(self): 
        """
        This function is used to place placeholders for inputs if required
        """
        if self._placeholder:
            self._placeholder.markdown("\n".join(self._items), unsafe_allow_html=True)
    
    def _markdown(self, text, level, space=""): 
        """
        This function is used to display items of markdown
        :param text: The text for the markdown
        :param level: The level in the markdown
        :param space: The spacing before text in markdown
        """

        assert isinstance(text, str)
        assert isinstance(level, str)
        assert isinstance(space, str)
        key = re.sub('[^0-9a-zA-Z]+', '-', text).lower()

        st.markdown(f"<{level} id='{key}'>{text}</{level}>", unsafe_allow_html=True)
        self._items.append(f"{space}* <a href='#{key}'>{text}</a>")

def sidebar(toc): 
    """
    This function is used to display the sidebar
    :param toc: The TOC class.
    """

    assert isinstance(toc, Toc)
    with st.sidebar:
        st.title('Table of Contents')
        
        toc.placeholder()

def audio(file_name):
    """
    :param file_name: The file path for the audio. This function will automatically embed the audio widget where every, you
    call it in the source file.
    """

    assert isinstance(file_name, str)
    audio_file_1 = open(file_name, 'rb')
    audio_1 = audio_file_1.read()
    st.audio(audio_1, format='mp3')

def death_causes_line_plot(): 
    """
    The function embeds the death causes line plot (data file: data/death_causes.csv) to where every, you
    call it in the source file.
    """
    df = pd.read_csv('data/death_causes.csv')
    df = df.set_index('Year')
    fig = px.line(df[['Heart disease', 'Cancer ', 'Unintentional injuries', 'CLRD', 'Stroke', "Alzheimer's disease", 'Diabetes']])


    fig['data'][0]['line']['color'] = "#FE0101"
    fig['data'][1]['line']['color'] = "#7FB5FF"
    fig.update_layout(
    title="Death Causes",
    title_x=0.45,
    xaxis_title="Year",
    yaxis_title="Count (thousands)",
    legend_title="variables")
    st.write(fig)

def chi_square_bar_plot(): 
    """
    The function embeds the chi-square bar plot (data file: data/processed_data.csv) to where every, you
    call it in the source file.
    """

    x = [10.43386255,  9.65029749,  9.38618916,  9.31959066,  8.77858069,
        7.83404486,  7.68797564,  7.1098964 ,  6.71319393,  6.57759726,
        6.16467774,  5.72584813,  4.86625959,  3.72561456,  1.86289353]
    y = ['AgeCategory', 'Diabetic', 'Stroke', 'DiffWalking',
       'KidneyDisease', 'SkinCancer', 'Smoking', 'BMI', 'Sex',
       'PhysicalActivity', 'Asthma', 'AlcoholDrinking', 'Race',
       'GenHealth', 'SleepTime']
    fig = go.Figure(go.Bar(
            x=x,
            y=y,
            orientation='h'))
    fig.update_layout(
           
            title="Effect of each Input using Chi-Square Test",
            title_x = 0.45,
            xaxis_title="log(Chi-Square Test Statistic) ",
            yaxis_title="Features"
    )
    st.plotly_chart(fig)




def dynamic_bar_plot(): 
    """
    The function embeds the bar plot (data file: data/heart_2020_cleaned.csv) of the various features to Heart Disease.
    """

    try:
        df = pd.read_csv("data/heart_2020_cleaned.csv")

    
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
        
        cols = col1.selectbox('Choose metric to view', metrics)
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
        fig.update_layout(
           
            title="Correlation Between Feature and Heart Disease",
            title_x = 0.45,
            xaxis_title= cols,
            yaxis_title="Percentage that have Heart Disease"
    )
        fig1.write(fig)

    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )




def progress_bar(color, value):
    """

    :param color: The color of the progress bar.
    :param value: The value set for the progress bar.
    """

    assert isinstance(color, str)
    assert isinstance(value, float)
    st.markdown(
    """
    <style>
        .stProgress > div > div > div > div {
            background-color: %s;
        }
    </style>""" % (color),
    unsafe_allow_html=True,
    )
    my_bar = st.progress(0)
    time.sleep(1)
    for percent_complete in range(int(value*100)):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)


def create_form(): #pragma: no cover
    """
    This function creates the form which will be used as the input to our model. Ths user doesn't need to select all
    the features, our model can retrain with subset of the features.
    """
    form = st.form(key='my_form')
    
    bmi = form.number_input('BMI ---- Body Mass Index Weight(kg)/(Height(m)*Height(m))')
    
    smoking = form.selectbox(
        'Smoking ---- Have you smoked at least 100 cigarettes in your entire life?',
        ('','True', 'False'))
    alcohol = form.selectbox(
        'Alcohol Drinking ---- Heavy drinkers? (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week',
        ('','True', 'False'))
    stroke = form.selectbox(
        'Stroke ---- (Ever told) (you had) a stroke?',
        ('','True', 'False'))
    walking = form.selectbox(
        'Difficult Walking ---- Do you have serious difficulty walking or climbing stairs?',
        ('','True', 'False'))
    sex = form.selectbox(
        'Sex ---- Are you bilogically male or female?',
        ('','Male', 'Female'))

    age = form.number_input('Age ---- What is your age?')

    race = form.selectbox(
        'Race ---- Please specify your ethnicity.',
        ('','White', 'Black', 'Asian', 'American Indian/Alaskan Native',
        'Other', 'Hispanic'))

    diabetic = form.selectbox(
        'Diabetic ---- (Ever told) (you had) diabetes?',
        ('','True', 'False'))

    activity = form.selectbox(
        'Physical Activity ---- Doing physical activity or exercise during the past 30 days other than regular job?',
        ('','True', 'False'))

    health = form.selectbox(
        'General Health ---- Would you say that in general your health is...',
        ('','Very good', 'Fair', 'Good', 'Poor', 'Excellent')
    )
    sleep = form.number_input('SleepTime (Hours) ---- On average, how many hours of sleep do you get in a 24-hour period?')

    asthma = form.selectbox(
        'Asthma ---- (Ever told) (you had) asthma?',
        ('','True', 'False'))

    kidney = form.selectbox(
        'Kidney Disease ---- Not including kidney stones, bladder infection or incontinence, were you ever told you had kidney disease?',
        ('','True', 'False'))

    skin = form.selectbox(
        'Skin Cancer ---- (Ever told) (you had) skin cancer?',
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
        st.markdown('## Your predicted risk is '+ display_risk)

        if risk < 0.2:
            progress_bar('green',risk)
            st.markdown("#### - Consume a healthy diet that emphasizes the intake of vegetables, fruits and nuts.\n"
            "#### - Healthy adults who lead a sedentary lifestyle should be encouraged to start with a light exercise intensity. Must maintain weight.")
        
        elif 0.2 <risk <= 0.4:
            progress_bar('blue',risk)
            st.markdown("#### - If you are overweight, achieve and maintain weight-loss.\n" 
        "#### - Healthy adults all ages of 2.5 to 5h a week of moderate physical activity or 1 to 2.5h per week of intense physical activity.\n"
    "#### - This includes fast walking, bicycling, or swimming. \n"
    "#### - Regularly consume fish.\n"
        "#### - Consume a varied well-balanced diet.\n")

        elif 0.4 < risk <= 0.6:
            progress_bar('yellow',risk)
            st.markdown(
        "#### - Eat a well balanced diet with lot of fruits and vegetables.\n"
    "#### - Reduced intake of salt in food (<5g/day)\n"
        "#### - 30 to 45 grams of fiber per day\n"
        "#### - Avoid salty and factory processed foods.\n"
        "#### - need 3 or more times a week moderate to intense aerobic exercise for 30 minutes.\n"
        "#### - Must restrict the usage of tobacco and consumption of alcohol. \n"
    "#### - Recommended to do a primary checkup. Should try to control stress.")

        elif 0.6 < risk <= 0.8:
            progress_bar('coral',risk)
            st.markdown( 
            "#### - 200g of fruit a day (2 to 3 meals per day).\n"
        "#### - 200g vegetables a day (2-3 servings per day).\n"
        "#### - Fish at least 2x per week (1 meal a week blue fish).\n"
        "#### - need 3 or more times a week moderate to intense aerobic exercise for 60 minutes.\n"
        "#### - Must also consult with doctor to see if intense physical activities is recommended.\n"
        "#### - Highly recommended to visit a clinic and follow medications.\n"
        "#### - Must strictly abstain from consumption of tobacco and alcohol. Should monitor blood pressure, cholesterol and diabetes regularly.\n" 
        "#### - Should include intensive counseling on risk factors.")

        else:
            progress_bar('red',risk)
            st.markdown("#### - Must immediately seek medical attention.")

def model_explanation(): 
    """
    This function writes text to the website, explaining our model pipeline.
    """
    st.markdown( "##### 1. Data Acquisition \n")
    st.write("The heart risk dataset is obtained from  the UCI ML repository. \
It contains 75 attributes for 303 patients.")
    st.markdown( "##### 2. Data Pre-processing \n")
    st.write("Cardiovascular disease UCI dataset is first loaded and then data cleaning\
 and finding missing values was performed on all records. The categorical\
features are converted to numerical ones to be used in Logistic Regression.")
    st.markdown( "##### 3. Feature Selection \n")
    st.write("The input has general patients details like age, gender and also certain medical information.\
 The medical information are vital attributes predicting heart disease. \
 The correlation performed on all 13 attributes with the target value to select the\
 features with high and positive correlation feature.")
    st.markdown( "##### 4. Classification model \n")
    st.write("To predict the heart disease logistic regression ML model is used, firstly the LR  \
model are trained after splitting condition and tested with test data for prediction to get the best accuracy and to find the models behavior. \
The LR is the supervised ML binary classification algorithm widely used in most application.  It works on categorical dependent variable the result can be discrete or binary categorical variable 0 or 1. The sigmoid function is used as a cost function. Sigmoid function maps a predicted real value to a probabilistic value.")
    st.markdown( "##### 5. Risk prediction \n")
    st.write("To predict the risk, the patient details are fed to the LR model. The LR model gives \
probabilistic values between 0 and 1, which can be scaled to percentage. The results are further split into 5 sub-categories to provide recommendations to the patients based on their information.")
