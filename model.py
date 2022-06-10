import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
import warnings

warnings.filterwarnings("ignore")


def model(user_data):
    """
    The functions runs the user data to a LogisticRegression model. The user doesn't need to upload all the user data,
    this function will dynamically train a new model with the given user data.

    :param user_data: The user data from the form.
    :return: The score of possible heart disease.
    """

    assert isinstance(user_data, pd.DataFrame)
    # pre-processing
    user_data = pd.Series(user_data, index=["HeartDisease", "BMI", "Smoking",
                                            "AlcoholDrinking",
                                            "Stroke",
                                            "DiffWalking",
                                            "Sex",
                                            "AgeCategory",
                                            "Race",
                                            "Diabetic",
                                            "PhysicalActivity",
                                            "GenHealth",
                                            "SleepTime",
                                            "Asthma",
                                            "KidneyDisease",
                                            "SkinCancer"])

    columns = ["Smoking", "Stroke", "DiffWalking", "AlcoholDrinking", "AgeCategory", "Diabetic", "GenHealth", "Sex",
               "Race", "PhysicalActivity", "SkinCancer", "KidneyDisease", "Asthma"]
    for col in columns:
        pkl_file = open('pretrain_model/' + col + '_encoder.pkl', 'rb')
        encoder = pickle.load(pkl_file)
        pkl_file.close()
        if user_data[col] != '':
            user_data[col] = encoder.transform((user_data[col],))[0]

    for col in ["BMI", "SleepTime"]:
        pkl_file = open('pretrain_model/' + col + '_encoder.pkl', 'rb')
        encoder = pickle.load(pkl_file)
        pkl_file.close()
        if user_data[col] != '':
            user_data[col] = encoder.transform(np.array(user_data[col], ).reshape(1, -1))[0][0]
    user_data = user_data.replace('', np.NaN)

    if user_data.isnull().any():  # re-train model
        # load data
        df = pd.read_csv('data/processed_data.csv')
        df.loc[len(df.index)] = user_data.values
        df = df.dropna(axis=1)

        X = df.drop(["HeartDisease"], axis=1)
        user_data = X.iloc[-1, :]
        X = X.iloc[:-1, :]
        y = df["HeartDisease"][:-1]
        y = y.astype('int')
        # train & test split
        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.20,
                                                            random_state=12)

        model = LogisticRegression()
        model.fit(x_train, y_train)

        score = model.score(x_test, y_test)
        output = model.predict_proba(user_data.values.reshape(1, -1))[0]

        return score, output[0]

    else:  # apply pre-train model
        user_data = user_data.drop(["HeartDisease"])
        model = pickle.load(open('pretrain_model/complete_model.sav', 'rb'))
        output = model.predict_proba(user_data.values.reshape(1, -1))[0]

        return 0.9141, output[0]


def age_tranform(age):
    """
    :param age: The age parameter converting from an integer to string interval.
    :return: String interval
    """

    assert isinstance(age, float) or isinstance(age, int)
    age = int(age)
    if age >= 55 and age <= 59:
        age = '55-59'
    elif age >= 80:
        age = '80 or older'
    elif age >= 65 and age <= 69:
        age = '65-69'
    elif age >= 75 and age <= 79:
        age = '75-79'
    elif age >= 40 and age <= 44:
        age = '40-44'
    elif age >= 70 and age <= 74:
        age = '70-74'
    elif age >= 60 and age <= 64:
        age = '60-64'
    elif age >= 50 and age <= 54:
        age = '50-54'
    elif age >= 45 and age <= 49:
        age = '45-49'
    elif age <= 24:
        age = '18-24'
    elif age >= 35 and age <= 39:
        age = '35-39'
    elif age >= 30 and age <= 34:
        age = '30-34'
    elif age >= 25 and age <= 29:
        age = '25-29'
    return age


if __name__ == '__main__':
    user_data = {
        "HeartDisease": "False",
        "BMI": 33,
        "Smoking": "False",
        "AlcoholDrinking": "False",
        "Stroke": "False",
        "DiffWalking": "True",
        "Sex": "Male",
        "AgeCategory": "80 or older",
        "Race": "White",
        "Diabetic": "True",
        "PhysicalActivity": "True",
        "GenHealth": "Poor",
        "SleepTime": 5,
        "Asthma": "False",
        "KidneyDisease": "True",
        "SkinCancer": "True",
    }
    score, prob = model(user_data)
    model(user_data)
    print(score, prob)
