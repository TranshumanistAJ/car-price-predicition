# Car Price Prediction App

 [Car Price Prediction](https://car-price-predicition.onrender.com) is a web-based application developed using **Streamlit** that predicts the price of used cars based on several features. It includes data preprocessing, exploratory data analysis, feature selection, hypothesis testing, and model deployment. The app is modularized into multiple pages for better usability and analysis workflow.

---

## 📌 Table of Contents

- [Project Overview](#project-overview)
- [Workflow](#workflow)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Model and Preprocessing](#model-and-preprocessing)
- [Streamlit Caching](#streamlit-caching)
- [Screenshots](#screenshots)
- [How to Run Locally](#how-to-run-locally)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)

---

## 🧾 Project Overview

This Car Price Prediction App allows users to:

- Understand the structure and insights of the dataset.
- Explore correlations among variables.
- Perform hypothesis tests to see how features relate to the selling price.
- Input custom vehicle parameters and predict the car's price using a trained machine learning model.

The target variable is **`selling_price`**, and the model is trained on cleaned and preprocessed data derived from an original used car dataset.

---

## 🔄 Workflow

The complete data and model pipeline follow this sequence:

1. **Data Collection**  
   - Raw data is loaded from CSV files located in the `datasets/` directory.

2. **Data Cleaning & Feature Engineering**  
   - Done in Jupyter notebooks located in `jupyter_notebooks/`.
   - Includes handling missing values, converting categorical variables, and feature extraction.

3. **Exploratory Data Analysis (EDA)**  
   - Includes distribution analysis, correlation matrix, and boxplots to detect outliers.

4. **Hypothesis Testing**  
   - Users interactively test how specific features (e.g., year, fuel type) influence price.

5. **Model Training**  
   - `RandomForestRegressor` from scikit-learn is used for training.
   - Trained on processed features with optimal hyperparameters.

6. **Deployment**  
   - Final model is integrated into Streamlit using a multi-page architecture.

---