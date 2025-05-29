import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import r2_score
import joblib

def train_pipeline():
    """
    Train a Gradient Boosting Regressor pipeline with hyperparameter optimization.
    
    Returns:
        best_model: Trained model with best hyperparameters.
        train_r2: R² score on training set.
        test_r2: R² score on test set.
    """
    # Load processed dataset
    df = pd.read_csv('../../datasets/processed_car_data.csv')
    
    # Define features and target
    X = df.drop(['Selling_Price(lacs)', 'Car_Name'], axis=1)
    y = df['Selling_Price(lacs)']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Define model and hyperparameter grid
    model = GradientBoostingRegressor(random_state=42)
    param_grid = {
        'n_estimators': [100, 200, 300],  # Number of trees
        'learning_rate': [0.01, 0.1, 0.2],  # Step size for updates
        'max_depth': [3, 5, 7],  # Maximum depth of trees
        'min_samples_split': [2, 5, 10],  # Minimum samples to split
        'min_samples_leaf': [1, 2, 4],  # Minimum samples at leaf
        'subsample': [0.8, 0.9, 1.0]  # Fraction of samples for fitting
    }
    
    # Rationale for hyperparameter choices:
    # - n_estimators: Tested 100-300 to balance model complexity and training time.
    # - learning_rate: Included lower (0.01) for stability, higher (0.2) for faster convergence.
    # - max_depth: 3-7 to capture complex patterns without excessive overfitting.
    # - min_samples_split/leaf: Varied to control tree growth and prevent overfitting.
    # - subsample: 0.8-1.0 to introduce stochasticity and improve generalization.
    
    # Perform GridSearchCV
    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='r2', n_jobs=-1)
    grid_search.fit(X_train, y_train)
    
    # Best model
    best_model = grid_search.best_estimator_
    
    # Predictions
    y_train_pred = best_model.predict(X_train)
    y_test_pred = best_model.predict(X_test)
    
    # Evaluate
    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)
    
    # Save model
    joblib.dump(best_model, '../../outputs/gradient_boosting.pkl')
    
    return best_model, train_r2, test_r2