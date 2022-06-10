import model as m
import source as s
# import numpy as np
import functions as f

import pytest
from unittest.mock import patch

# import streamlit
import warnings
warnings.filterwarnings("ignore")



def test_source():
    assert s.main() == None

user_data = {
            "HeartDisease":0,
            "BMI":-1.844750158718647,
            "Smoking":1,
            "AlcoholDrinking":0,
            "Stroke":0,
            "DiffWalking":0,
            "Sex":0,
            "AgeCategory":7,
            "Race":5,
            "Diabetic":2,
            "PhysicalActivity":1,
            "GenHealth":4,
            "SleepTime":-1.4603535207211777,
            "Asthma":1,
            "KidneyDisease":0,
            "SkinCancer":1,
            }
def test_model(user_data):
    assert isinstance(m.model(user_data),float)
    assert 0 <= m.model(user_data)[0] <= 1.
    assert 0 <= m.model(user_data)[1] <= 1.
def test_age_transform():
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

@pytest.mark.skip(reason="no way of currently testing this")
def test_model(HeartDisease, BMI, Smoking, AlcoholDrinking, Stroke, \
                            DiffWalking, Sex, AgeCategory, Race, Diabetic, \
                            PhysicalActivity, GenHealth, SleepTime, Asthma, \
                            KidneyDisease, SkinCancer):
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



# test_model(0,-1.844750158718647,1,0,0,0,0,7,5,2,1,4,-1.4603535207211777,1,0,1)
    

# @patch('streamlit.audio')
# def test_audio(placeholder):
#     f.audio('audio/speech_1.mp3')
#     f.audio('audio/speech_2.mp3')


# @patch('streamlit.sidebar')
# def test_sidebar(placeholder):
#     toc = f.Toc()
#     f.sidebar(toc)

# @patch('streamlit.write')
# def test_line_plot_2(placeholder):
#     f.line_plot_2()

# @patch('streamlit.plotly_chart')
# def test_bar2(placeholder):
#     f.bar2()

'''
still need functions to test 
bar_plot()
progress_bar(color, value)
create_form()
model_explanation()

'''


