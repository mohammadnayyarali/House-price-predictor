from pathlib import Path

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from backend.predictor import Predictor
from backend.schemas import PredictionRequest, PredictionResult

app = FastAPI(
    title="House Price Prediction API",
    description="Predict house prices from area, bedrooms, bathrooms, year built, garage, and location.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

frontend_dir = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/static", StaticFiles(directory=str(frontend_dir)), name="static")

@app.get("/")
def read_index():
    return FileResponse(frontend_dir / "index.html")

predictor = Predictor()

@app.post("/predict", response_model=PredictionResult)
def predict_price(payload: PredictionRequest):
    try:
        prediction = predictor.predict(payload)
        return PredictionResult(price=prediction)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=503, detail=str(exc))
    except Exception:
        raise HTTPException(status_code=500, detail="Prediction failed due to server error.")
