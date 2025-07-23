from ml_models.traffic import train_traffic_model
from ml_models.flood import train_flood_model
from ml_models.water import train_water_model

train_traffic_model("ml_models/sample_traffic.csv")
train_flood_model("ml_models/sample_flood.csv")
train_water_model("ml_models/sample_water.csv")

print("All models trained and saved!")
