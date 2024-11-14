from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load your trained Gradient Boosting model (replace with the actual model file)
model = joblib.load('tuned_gbr_model.pkl')

# Initialize FastAPI app
app = FastAPI()

# Define the input schema (adjust based on your model's expected features)
class HouseFeatures(BaseModel):
    CRIM: float
    ZN: float
    INDUS: float
    CHAS: float
    NOX: float
    RM: float
    DIS: float
    RAD: float
    TAX: float
    PTRATIO: float
    B: float
    LSTAT: float

# Define prediction endpoint
@app.post("/predict/")
async def predict(features: HouseFeatures):
    feature_array = np.array([
        [
            features.CRIM, features.ZN, features.INDUS, features.CHAS,
            features.NOX, features.RM, features.DIS, features.RAD,
            features.TAX, features.PTRATIO, features.B, features.LSTAT
        ]
    ])
    prediction = model.predict(feature_array)
    return {"predicted_price": prediction[0]}