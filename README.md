# Predictiong-House-Prices
This project aims to predict house prices based on various characteristics using machine learning techniques. The pipeline includes data exploration, preprocessing, model training, hyperparameter optimization, and deployment through a Flask web application and API.

## Data Exploration
- Conducted exploratory data analysis (EDA) to understand the dataset and identify the most significant features.
- Removed irrelevant or redundant features to enhance model performance.

## Data Preprocessing:
- Cleaned and transformed the dataset to ensure it is suitable for training.
- Handled missing values, scaled numeric data, and encoded categorical features.

##Model Training:
- Trained two machine learning models: Random Forest Regressor & XGBoost Regressor.
- Performed hyperparameter optimization for both models using Optuna, with cross-validation to validate results.

## Model Selection:
- Evaluated the models on a validation set.
- XGBoost outperformed Random Forest in terms of accuracy and was selected for deployment.

## Deployment:
- Integrated the XGBoost model into a FastAPI web application.
- Created an API endpoint to predict house prices based on input characteristics.
