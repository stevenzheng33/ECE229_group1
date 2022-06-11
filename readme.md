# Cardio Care: A Heart Disease Analysis
![alt text](/readme_images/cover.png "Title")
## Summary
Cardio Care provides a platform for users to learn about the risk and causes of heart disease. Our main application takes in easily-accessible features and output the predicted risk and corresponding recommendations for the user. 

## Techonology Stack
Our application is built on streamlit with customizable modules including plotly ans scikit learn. The source file is deployed on an EC2 instance in the cloud.

![alt text](/readme_images/tech_stack.png "Title")

## Cloud Architecture

![alt text](/readme_images/aws_design.png "Title")

## Requirement

- Coverage 6.4.1
- Numpy 1.22.4
- Python 3.8
- Pandas 1.4.2
- Plotly 5.8.2
- Streamlit 1.10
- Sklearn 1.1.1
  
## Test Suite

Below is the coverage report for our code repository.

![alt text](/readme_images/coverage.png "Title")

To generate the coverage report first run `coverage run test_model.py` then run `coverage report -m `