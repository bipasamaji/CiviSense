import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'traffic_model.joblib') 

def train_traffic_model(csv_path):
    df = pd.read_csv(csv_path, parse_dates=['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    x = df[['hour']]
    y = df['congestion_level']
    model = LinearRegression()
    model.fit(x, y)
    joblib.dump(model, MODEL_PATH)
    print("Traffic Model trained and saved.")

def predict_traffic(hour):
    model = joblib.load(MODEL_PATH)
    return float(model.predict(np.array([[hour]]))[0])

