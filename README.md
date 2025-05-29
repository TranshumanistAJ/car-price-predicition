# Car Price Prediction

## Project Overview
This project develops a Streamlit-based Data App to predict car selling prices based on attributes such as Present Price, Kilometers Driven, Fuel Type, Seller Type, Transmission, Past Owners, and Age. The app provides interactive data visualizations and a prediction interface to meet business requirements, delivering actionable insights for car dealerships and individual sellers.

## Dataset Content
- **Source**: [Kaggle Vehicle Dataset](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho)
- **Attributes**:
  - **Car_Name**: Name of the car
  - **Selling_Price(lacs)**: Selling price in lacs
  - **Present_Price(lacs)**: Current market price in lacs
  - **Kms_Driven**: Kilometers driven
  - **Fuel_Type**: Petrol, Diesel, or CNG
  - **Seller_Type**: Dealer or Individual
  - **Transmission**: Manual or Automatic
  - **Past_Owners**: Number of previous owners
  - **Age**: Age of the car (derived from Year)

## Business Requirements
- **BR1**: Conduct a study to understand how car attributes correlate with selling price.
- **BR2**: Predict the selling price of a car based on its attributes.

## Project Hypothesis
1. **Hypothesis 1**: Cars with lower age and fewer kilometers driven have higher selling prices.
   - **Rationale**: Newer cars with less wear are typically more valuable.
2. **Hypothesis 2**: Diesel cars have higher selling prices than petrol cars.
   - **Rationale**: Diesel cars often have better fuel efficiency and durability, increasing market value.
3. **Hypothesis 3**: Manual transmission cars have lower selling prices than automatic ones.
   - **Rationale**: Automatic cars are often preferred for convenience, commanding higher prices.

## Validation of Hypotheses
- **Hypothesis 1**: Validated via negative correlations in the heatmap (Age: -0.24, Kms_Driven: -0.15 with Selling Price).
- **Hypothesis 2**: Confirmed with a t-test (p-value < 0.05) and box plot showing higher median prices for diesel cars.
- **Hypothesis 3**: Validated via violin plot showing automatic cars have higher median selling prices.

## Rationale for Mapping Business Requirements
- **BR1**: Addressed through interactive visualizations (heatmap, scatter, box, violin plots) in the EDA notebook and Findings dashboard page.
- **BR2**: Addressed by training a Gradient Boosting Regressor with hyperparameter optimization (Model Training notebook and Prediction Interface page).

## ML Business Case
- **Aim**: Predict car selling prices using regression.
- **Learning Method**: Supervised learning with Gradient Boosting Regressor (ensemble method combining decision trees).
- **Ideal Outcome**: Achieve R² ≥ 0.85 on the test set, indicating high predictive accuracy.
- **Success Metrics**: R² score, Mean Absolute Error (MAE), and Actual vs Predicted plot.
- **Model Output**: Continuous value representing predicted selling price in lacs.
- **Relevance**: Enables accurate pricing for car dealerships and sellers, maximizing profit and market competitiveness.
- **Training Data**: Processed dataset with one-hot encoded categorical variables (Fuel_Type, Seller_Type, Transmission) and scaled numerical features (Present_Price, Kms_Driven, Past_Owners, Age).
- **Heuristics**: Hyperparameter optimization using GridSearchCV with six parameters to balance bias and variance.

## Dashboard Design
- **Project Summary**: Overview, dataset description, and client requirements (text).
- **Findings**: Interactive visualizations (heatmap, scatter, box, violin plots) with interpretations addressing BR1.
- **Prediction Interface**: Input widgets for car attributes and prediction output for BR2.
- **Hypothesis and Validation**: Hypothesis statements with statistical validation (t-test, visualizations).
- **ML Metrics**: Model performance metrics (R² scores, Actual vs Predicted plot).

## Development Process
- **Data Collection**: Loaded dataset from Kaggle (`1_data_collection.ipynb`).
- **Data Cleaning**: Handled missing values, transformed Year to Age, renamed columns (`2_data_cleaning.ipynb`).
- **Feature Engineering**: One-hot encoded categorical variables, scaled numerical features (`3_feature_engineering.ipynb`).
- **EDA**: Created interactive visualizations to analyze correlations (`4_eda.ipynb`).
- **Model Training**: Trained Gradient Boosting Regressor with GridSearchCV, evaluating R² and plotting Actual vs Predicted (`5_model_training.ipynb`).
- **Dashboard**: Built with Streamlit, organized in `app_pages/` and `src/` folders, deployed on Heroku.
- **Hyperparameter Rationale**:
  - `n_estimators` (100, 200, 300): Balances model complexity and training time.
  - `learning_rate` (0.01, 0.1, 0.2): Tests stability vs. convergence speed.
  - `max_depth` (3, 5, 7): Captures complex patterns without overfitting.
  - `min_samples_split` (2, 5, 10): Controls tree splitting for generalization.
  - `min_samples_leaf` (1, 2, 4): Prevents overfitting by limiting leaf size.
  - `subsample` (0.8, 0.9, 1.0): Introduces stochasticity for robustness.

## Project Structure

!!!!!!




## Deployment
- Deployed on Heroku.
- Requirements: `requirements.txt`, `Procfile`, `runtime.txt`, `setup.sh`.

## Version Control
- Managed with Git, with clear commit messages for each feature/fix (e.g., data cleaning, model training, dashboard pages).

## Accessibility
- The dashboard uses semantic structure, clear navigation, and interactive visualizations to ensure accessibility and positive user experience.

## How to Execute
1. **Set Up Repository**:
   - Clone the repository.
   - Initialize Git: `git init`.

2. **Install Dependencies**:
   - Create virtual environment: `python -m venv venv`.
   - Activate: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows).
   - Install requirements: `pip install -r requirements.txt`.

3. **Run Notebooks**:
   - Open `jupyter_notebooks/version1/` and run notebooks in order (1 to 5).
   - Ensure `car_data.csv` is in `datasets/`.

4. **Run Streamlit App**:
   - Run `streamlit run app.py`.

5. **Deploy to Heroku**:
   - Create Heroku app: `heroku create`.
   - Push: `git push heroku main`.