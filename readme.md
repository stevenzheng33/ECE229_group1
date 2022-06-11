# Cardio Care: A Heart Disease Analysis
![alt text](/readme_images/cover.png "Title")
## Summary
Cardio Care provides a platform for users to learn about the risk and causes of heart disease. Our main application takes in easily-accessible features and output the predicted risk and corresponding recommendations for the user. Our website is designed with accessibility in mind with features such as identifying color tones and audio transcription.

## Techonology Stack
Our application is built on streamlit with customizable modules including plotly ans scikit learn. The source file is deployed on an EC2 instance in the cloud.

![alt text](/readme_images/tech_stack.png "Title")

## Cloud Architecture
We use route 53 as a DNS service that leads to a ELB that directs traffic into out web EC2 auto scaling group. AWS RDS is used to store user data with permission and Amazon Polly is used to transribe the texts to audio. Our heavy workload is handed off to computational instances through Amazon SQS.
![alt text](/readme_images/aws_design.png "Title")

## Documentation
We used sphinx to build a fully functional documentation. In the root directory run `open docs/index.html` to view the documentation webpage. Choose between the function and model module to view the description for every piece of our project.


## Folder Structure
``` bash
.
├── audio                             # Audio File
│   ├── speech_1.mp3
│   └── speech_2.mp3
├── data                              # Source Data
│   ├── death_causes.csv
│   ├── heart_2020_cleaned.csv
│   └── processed_data.csv
├── doc                               # Sphinx Documentation
├── functions.py                      # Uility functions file
├── model.py                          # Logistic Model file
├── pretrain_model                    # Pretrained models to speed up the application
├── readme.md
├── readme_images     
│   ├── aws_design.png
│   ├── cover.png
│   ├── coverage.png
│   └── tech_stack.png
├── source.py                         # Streamlit Index File
└── test_model.py                     # Testing file
```

## Requirement

- Coverage 6.4.1
- Numpy 1.22.4
- Python 3.8
- Pandas 1.4.2
- Plotly 5.8.2
- Streamlit 1.10
- Sklearn 1.1.1

## View our Application
You can either access our hosted app using the link in the beginning or run `streamlit run source.py` in the root directory.
  
## Test Suite

Below is the coverage report for our code repository.

![alt text](/readme_images/coverage.png "Title")

To generate the coverage report first run `coverage run test_model.py` then run `coverage report -m `