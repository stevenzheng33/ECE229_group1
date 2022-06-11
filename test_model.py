import model as m
import numpy as np
import functions as f
import pytest
from unittest.mock import patch
import streamlit

def test_age_transform():
    '''
    Method used to test the age trasnform function
    '''
    assert m.age_tranform(56) == '55-59'
    assert m.age_tranform(81) == '80 or older'
    assert m.age_tranform(67) == '65-69'
    assert m.age_tranform(76) == '75-79'
    assert m.age_tranform(42) == '40-44'
    assert m.age_tranform(72) == '70-74'
    assert m.age_tranform(61) == '60-64'
    assert m.age_tranform(51) == '50-54'
    assert m.age_tranform(46) == '45-49'
    assert m.age_tranform(19) == '18-24'
    assert m.age_tranform(36) == '35-39'
    assert m.age_tranform(31) == '30-34'
    assert m.age_tranform(26) == '25-29'


def test_model():
    '''
    Method used to test the model function
    '''
    user_data = {
                "HeartDisease":"False",
                "BMI":33,
                "Smoking":"False",
                "AlcoholDrinking":"False",
                "Stroke":"False",
                "DiffWalking":"True",
                "Sex":"Male",
                "AgeCategory":"80 or older",
                "Race":"White",
                "Diabetic":"True",
                "PhysicalActivity":"True",
                "GenHealth":"Poor",
                "SleepTime":5,
                "Asthma":"False",
                "KidneyDisease":"True",
                "SkinCancer":"True",
                }
    assert m.model(user_data)[0] == 0.9141
    # assert m.model(user_data)[1] == 0.3551001411628071

def test_model_with_null():
    '''
    Method used to test the model function with null value
    '''
    user_data = {
                "HeartDisease":"False",
                "BMI":np.nan,
                "Smoking":"False",
                "AlcoholDrinking":"False",
                "Stroke":"False",
                "DiffWalking":"True",
                "Sex":"Male",
                "AgeCategory":"80 or older",
                "Race":"White",
                "Diabetic":"True",
                "PhysicalActivity":"True",
                "GenHealth":"Poor",
                "SleepTime":5,
                "Asthma":"False",
                "KidneyDisease":"True",
                "SkinCancer":"True",
                }
    assert m.model(user_data)[0] == 0.9143826513860441
    assert m.model(user_data)[1] > 0.362846179685 - 0.05 and m.model(user_data)[1] < 0.362846179685 + 0.05


@patch('streamlit.audio')
def test_audio(placeholder):
    '''
    Function used to test the audio function
    '''
    f.audio('audio/speech_1.mp3')
    f.audio('audio/speech_2.mp3')


@patch('streamlit.sidebar')
def test_sidebar(placeholder):
    '''
    Function used to test the sidebar function
    '''
    toc = f.Toc()
    f.sidebar(toc)

@patch('streamlit.write')
def test_line_plot_2(placeholder):
    '''
    Function used to test the plotting of line function
    '''
    f.death_causes_line_plot()

@patch('streamlit.plotly_chart')
def test_bar2(placeholder):
    '''
    Function used to test plotting the bar function
    '''
    f.chi_square_bar_plot()

def test_Toc():
    '''
    Method used to test the Toc class
    '''
    toc = f.Toc()
    toc.title('test')
    toc.header('test')
    toc.subheader('test')
    toc.placeholder(False)
    toc.generate()

@patch('streamlit.write')
def test_death_causes_line_plot(placeholder):
    '''
    Method used to test the death causes line plot function
    '''
    f.death_causes_line_plot()

@patch('streamlit.plotly_chart')
def test_chi_square_bar_plot(placeholder):
    '''
    Method used to test the chi square bar plot function
    '''
    f.chi_square_bar_plot()

def test_dynamic_bar_plot():
    '''
    Method used to test the dynamic bar plot function
    '''
    f.dynamic_bar_plot()

def test_create_form():    
    '''
    Method used to test the create form function
    '''
    f.create_form()

def test_model_explanation():
    '''
    Method used to test the model explanation function
    '''
    f.model_explanation()

def test_progress_bar():
    '''
    Method used to test the progress bar function
    '''
    f.progress_bar('red', 0.3)


test_age_transform()
test_model()
test_model_with_null()
test_audio()
test_sidebar()
test_line_plot_2()
test_bar2()
test_Toc()
test_death_causes_line_plot()
test_chi_square_bar_plot()
test_dynamic_bar_plot()
test_progress_bar()
test_create_form()
test_model_explanation()