# Deployment Guide

This project supports both container-based and platform deployment.

## Render Deployment

Render is configured using `render.yaml` at the root of the project or in this folder.

Steps:
1. Commit the repository to GitHub.
2. Create a new Render service and connect your GitHub repository.
3. Use the `render.yaml` manifest to auto-deploy the Python web service.
4. Ensure `models/house_price_model.joblib` is present in the repo or generated before deployment.

The service uses:
- `buildCommand`: `pip install --no-cache-dir -r requirements.txt`
- `startCommand`: `uvicorn backend.app:app --host 0.0.0.0 --port $PORT`
- `MODEL_PATH`: `models/house_price_model.joblib`

## Docker Deployment

Build locally:

```bash
docker build -t house-price-prediction .
```

Run locally:

```bash
docker run -p 8000:8000 house-price-prediction
```

Then open `http://127.0.0.1:8000`.

## Local Deployment Notes

- Train the model locally before deploying:
  - `python model_training/train.py`
- If you use a `.env` file, copy from `.env.example`.

## Optional Railway or Other Platforms

- Railway: connect the GitHub repo and use the existing `Dockerfile`.
- Any platform that supports Python and FastAPI can run the application with the same commands.
