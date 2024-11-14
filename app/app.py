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
    bedrooms: int
    bathrooms: float
    sqft_living: int
    sqft_lot: int
    floors: float
    condition: int
    grade: int
    sqft_above: int
    sqft_basement: int
    yr_built: int
    yr_renovated: int
    zipcode: int

# Define prediction endpoint
@app.post("/predict/")
async def predict(features: HouseFeatures):
    feature_array = np.array([
        [
            features.bedrooms, features.bathrooms, features.sqft_living, features.sqft_lot,
            features.floors, features.condition, features.grade, features.sqft_above,
            features.sqft_basement, features.yr_built, features.yr_renovated, features.zipcode
        ]
    ])
    prediction = model.predict(feature_array)
    return {"predicted_price": prediction[0]}