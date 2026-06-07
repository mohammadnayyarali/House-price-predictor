<<<<<<< HEAD
# House Price Prediction System

A production-grade end-to-end system for predicting house prices using a machine learning model, serving predictions through a REST API, and presenting a clean frontend web experience.

## Project Structure
- `backend/` — API layer built with FastAPI
- `frontend/` — Web UI for collecting user input and displaying predictions
- `model_training/` — Data cleaning, exploration, model training, and evaluation
- `data/` — Dataset assets and sample data
- `models/` — Saved serialized models and model artifacts
- `artifacts/` — Optional generated artifacts such as reports and plots
- `pipelines/` — Modular ML pipeline stages for ingestion, preprocessing, training, evaluation, and serialization
- `utils/` — Shared utilities and helpers
- `config/` — Deployment, environment, and settings files
- `logs/` — Logging outputs and runtime traces
- `deployment/` — Docker and cloud deployment configuration

## Quick Start
1. Create a Python environment
2. Install dependencies: `pip install -r requirements.txt`
2.5. Copy `.env.example` to `.env` and adjust settings if needed
3. Train the model: `python model_training/train.py`
4. Run the backend: `uvicorn backend.app:app --reload --host 0.0.0.0 --port 8000`
5. Open `http://127.0.0.1:8000` in your browser or deploy the service

## Deployment

### Render
- Use the included `render.yaml` manifest in the repository root or `deployment/render.yaml`.
- Deploy the app as a Python web service.
- Build command: `pip install --no-cache-dir -r requirements.txt`
- Start command: `uvicorn backend.app:app --host 0.0.0.0 --port $PORT`
- Environment variable: `MODEL_PATH=models/house_price_model.joblib`

### Docker
- Build image: `docker build -t house-price-prediction .`
- Run container: `docker run -p 8000:8000 house-price-prediction`
- Open browser at `http://127.0.0.1:8000`

### Local Deployment Notes
- Ensure the model artifact exists: `models/house_price_model.joblib`
- Copy `.env.example` to `.env` if you want environment override support.

## Dataset Selection and Training Workflow
- The sample dataset is stored in `data/house_prices_sample.csv`.
- The training pipeline cleans data, engineers features, and compares multiple regressors.
- `model_training/train.py` evaluates both Linear Regression and Random Forest models, then saves the best-performing model to `models/house_price_model.joblib`.
- The backend is now configured to load models dynamically from `config/settings.py`, with safe fallback handling if the trained artifact is missing.
- The deployment manifest trains the model during build so production does not depend on a pre-existing model file.
- Optionally run EDA with `python -c "from model_training.train import main; main(run_eda=True)"` to generate correlation and pair plots in `logs/`.
=======
# Hoouse-price-predictor
End-to-end ML + Web App for house price prediction
>>>>>>> cca049b7b2b696176df183a319a1bbdd09039d09
