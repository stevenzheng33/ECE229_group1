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

test_list = [   ("False",33,"False","False","False","True","Male","80 or older","White","True","True","Poor",5,"False","True","True"),
                ("False",0,"True","False","False","True","Male","80 or older","White","True","True","Poor",12,"False","True","True")
                
                
            ]

@pytest.mark.parametrize('HeartDisease, BMI, Smoking, AlcoholDrinking, Stroke, \
                            DiffWalking, Sex, AgeCategory, Race, Diabetic, \
                            PhysicalActivity, GenHealth, SleepTime, Asthma, \
                            KidneyDisease, SkinCancer',
                            test_list
                            )
def test_model(HeartDisease, BMI, Smoking, AlcoholDrinking, Stroke, \
                            DiffWalking, Sex, AgeCategory, Race, Diabetic, \
                            PhysicalActivity, GenHealth, SleepTime, Asthma, \
                            KidneyDisease, SkinCancer):
    '''
    Method used to test the functions in model
    '''
    user_data = {
                "HeartDisease":HeartDisease,
                "BMI":BMI,
                "Smoking":Smoking,
                "AlcoholDrinking":AlcoholDrinking,
                "Stroke":Stroke,
                "DiffWalking":DiffWalking,
                "Sex":Sex,
                "AgeCategory":AgeCategory,
                "Race":Race,
                "Diabetic":Diabetic,
                "PhysicalActivity":PhysicalActivity,
                "GenHealth":GenHealth,
                "SleepTime":SleepTime,
                "Asthma":Asthma,
                "KidneyDisease":KidneyDisease,
                "SkinCancer":SkinCancer,
                }
    assert 0 <= m.model(user_data)[0] <= 1.
    assert 0 <= m.model(user_data)[1] <= 1.


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
    f.line_plot_2()

@patch('streamlit.plotly_chart')
def test_bar2(placeholder):
    '''
    Function used to test plotting the bar function
    '''
    f.bar2()

'''
still need functions to test 
bar_plot()
progress_bar(color, value)
create_form()
model_explanation()

'''

# @patch('streamlit.columns.write')
# def test_bar_plot(placeholder):
#     f.bar_plot()

# @patch('streamlit.progress')
# def test_progress_bar(placeholder):
#     f.progress_bar('red', 50)
