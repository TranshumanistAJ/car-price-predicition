# car-price-predicition

## Project Overview
This project develops a Streamlit-based Data App to predict car selling prices based on attributes such as Present Price, Kilometers Driven, Fuel Type, Seller Type, Transmission, Past Owners, and Age. The app provides data visualizations and a prediction interface to meet business requirements.
Dataset Content

Source: Kaggle (https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho)
Attributes:
Car_Name: Name of the car
Selling_Price(lacs): Selling price in lacs
Present_Price(lacs): Current market price in lacs
Kms_Driven: Kilometers driven
Fuel_Type: Petrol, Diesel, or CNG
Seller_Type: Dealer or Individual
Transmission: Manual or Automatic
Past_Owners: Number of previous owners
Age: Age of the car (derived from Year)



Business Requirements

BR1: Conduct a study to understand how car attributes correlate with selling price.
BR2: Predict the selling price of a car based on its attributes.

Project Hypothesis

Cars with lower age and fewer kilometers driven have higher selling prices.
Diesel cars have higher selling prices than petrol cars.
Manual transmission cars have lower selling prices than automatic ones.

Validation of Hypotheses

Hypothesis 1: Validated via negative correlations in the heatmap.
Hypothesis 2: Confirmed with a t-test (p-value < 0.05) and box plot analysis.
Hypothesis 3: Validated via box plot showing higher prices for automatic cars.

Rationale for Mapping Business Requirements

BR1: Addressed through correlation heatmaps and scatter/box plots (EDA notebook).
BR2: Addressed by training a Gradient Boosting Regressor (Model Training notebook).

ML Business Case

Aim: Predict car selling prices.
Learning Method: Regression (Gradient Boosting).
Ideal Outcome: R² ≥ 0.85 on test set.
Success Metrics: R² score, Actual vs Predicted plot.
Model Output: Predicted price in lacs.
Relevance: Helps clients price cars accurately.
Training Data: Processed dataset with encoded and scaled features.

Dashboard Design

Project Summary: Overview, dataset description, and client requirements.
Findings: Visualizations (heatmap, scatter, box plots) with interpretations.
Prediction Interface: Input widgets for car attributes and prediction output.
Hypothesis and Validation: Hypothesis statements and statistical validation.
ML Metrics: Model performance metrics and Actual vs Predicted plot.

Development Process

Data Collection: Loaded dataset from Kaggle.
Data Cleaning: Transformed Year to Age, renamed columns.
Feature Engineering: Encoded categorical variables, scaled numerical features.
EDA: Created visualizations to analyze correlations.
Model Training: Used GridSearchCV with 6 hyperparameters for Gradient Boosting.
Dashboard: Built with Streamlit, deployed on Heroku.

Project Structure
car-price-prediction/
├── app_pages/
│   ├── __init__.py
│   ├── page_project_summary.py
│   ├── page_findings.py
│   ├── page_prediction_interface.py
│   ├── page_hypothesis_validation.py
│   ├── page_ml_metrics.py
├── src/
│   ├── __init__.py
│   ├── machine_learning/
│   │   ├── evaluate_reg.py
│   │   ├── train_pipeline.py
├── jupyter_notebooks/
│   ├── version1/
│   │   ├── 1_data_collection.ipynb
│   │   ├── 2_data_cleaning.ipynb
│   │   ├── 3_feature_engineering.ipynb
│   │   ├── 4_eda.ipynb
│   │   ├── 5_model_training.ipynb
├── datasets/
│   ├── car_data.csv
├── app.py
├── Procfile
├── requirements.txt
├── runtime.txt
├── setup.sh
├── README.md

Deployment

Deployed on Heroku.
Requirements: requirements.txt, Procfile, runtime.txt, setup.sh.

Version Control

Managed with Git, with clear commit messages for each feature.

Accessibility

The dashboard uses clear navigation and semantic structure for accessibility.

How to Execute

Set Up Repository:
Clone the repository.
Initialize Git: git init.


Install Dependencies:
Create virtual environment: python -m venv venv.
Activate: source venv/bin/activate (Linux/Mac) or venv\Scripts\activate (Windows).
Install requirements: pip install -r requirements.txt.


Run Notebooks:
Open jupyter_notebooks/version1/ and run notebooks in order (1 to 5).
Ensure car_data.csv is in datasets/.


Run Streamlit App:
Run streamlit run app.py.


Deploy to Heroku:
Create Heroku app: heroku create.
Push: git push heroku main.



