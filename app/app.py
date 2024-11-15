from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
from typing import List  # Import List for multiple house inputs
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Load your trained Gradient Boosting model (replace with the actual model file)
model = joblib.load('/app/tuned_gbr_model.pkl')

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
    AGE:float
    DIS: float
    RAD: float
    TAX: float
    PTRATIO: float
    B: float
    LSTAT: float

# Define prediction endpoint
@app.post("/predict/")
async def predict(features: List[HouseFeatures]):
    try:

        # Log the received features for debugging
        logging.debug(f"Received features: {features}")

        # Convert the input features into a Pandas DataFrame with the correct column names
        feature_dicts = [feature.dict() for feature in features] # convert each feature set to a dictionary
        feature_df = pd.DataFrame(feature_dicts) # convert the list of dictionaries into a DataFrame

        # Log the input DataFrame for debugging
        logging.debug(f"Input Feature DataFrame: \n{feature_df}")

        # Make the prediction using the model
        prediction = model.predict(feature_df) # pass the DataFrame to the model

        # Log the prediction
        logging.debug(f"Prediction: {prediction}")

        # Return the predictions as a JSON response
        return {"predicted_prices": prediction.tolist()}
    
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    


    