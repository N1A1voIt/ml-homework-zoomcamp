from typing import Any

from fastapi import FastAPI
from loader import load_model
from predict import predict,Lead
from pydantic import BaseModel
import hashlib

pipeline = load_model()
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/health")
def health() -> dict[str, Any]:
    return {
        "status": "ok"
    }

@app.post("/predict")
def prediction(lead: Lead) :
    return predict(pipeline,lead)
