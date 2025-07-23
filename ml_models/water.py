
import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "water_model.joblib")

def train_water_model(csv_path):
    df = pd.read_csv(csv_path)
    features = ['supply_hours', 'pressure']
    X = df[features]
    model = IsolationForest(contamination=0.1)
    model.fit(X)
    joblib.dump(model, MODEL_PATH)
    print("Water anomaly model trained and saved.")

def check_water_anomaly(supply_hours, pressure):
    model = joblib.load(MODEL_PATH)
    score = model.predict([[supply_hours, pressure]])
    return int(score[0]) == -1