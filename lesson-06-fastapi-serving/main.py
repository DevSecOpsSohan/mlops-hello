"""Serve the Iris model as a REST API — Lesson 06."""

from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Create the API app
app = FastAPI(title="Iris Classifier API")

# Load the trained model once, when the app starts
model = joblib.load("model.joblib")

# Map the model's number output (0/1/2) to human-readable names
SPECIES = ["setosa", "versicolor", "virginica"]


# Describe the shape of the input data we expect (4 measurements)
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/")
def home():
    """A simple health-check endpoint."""
    return {"message": "Iris model API is running. Go to /docs to try it."}


@app.post("/predict")
def predict(features: IrisFeatures):
    """Take 4 measurements, return the predicted species."""
    # Arrange the inputs the way the model expects: a list of rows
    data = [[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width,
    ]]

    prediction = model.predict(data)          # e.g. array([0])
    species_index = int(prediction[0])         # 0
    return {
        "prediction": species_index,
        "species": SPECIES[species_index],     # "setosa"
    }