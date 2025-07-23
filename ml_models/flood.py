import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "flood_model.joblib")

def train_flood_model(csv_path):
    df = pd.read_csv(csv_path)
    features = ['rainfall', 'drainage_capacity', 'elevation']
    X = df[features]
    y = df['risk_label']
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    print("Flood model trained and saved.")

def predict_flood_risk(rainfall, drainage_capacity, elevation):
    model = joblib.load(MODEL_PATH)
    pred = model.predict([[rainfall, drainage_capacity, elevation]])
    return pred[0]