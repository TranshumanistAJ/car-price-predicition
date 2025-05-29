import pandas as pd
import joblib
from sklearn.metrics import r2_score

def load_test_evaluation():
    df = pd.read_csv('../../datasets/processed_car_data.csv')
    X = df.drop(['Selling_Price(lacs)', 'Car_Name'], axis=1)
    y = df['Selling_Price(lacs)']
    model = joblib.load('../../outputs/gradient_boosting.pkl')
    y_pred = model.predict(X)
    return r2_score(y, y_pred)