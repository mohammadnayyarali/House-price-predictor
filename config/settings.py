import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

DATA_DIR = ROOT_DIR / "data"
MODELS_DIR = ROOT_DIR / "models"
ARTIFACTS_DIR = ROOT_DIR / "artifacts"
LOGS_DIR = ROOT_DIR / "logs"

MODEL_FILENAME = os.getenv("MODEL_FILENAME", "house_price_model.joblib")
MODEL_PATH = Path(os.getenv("MODEL_PATH", str(MODELS_DIR / MODEL_FILENAME)))
DATA_PATH = Path(os.getenv("DATA_PATH", str(DATA_DIR / "house_prices_sample.csv")))

API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", 8000))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
AUTO_TRAIN_ON_MISSING = os.getenv("AUTO_TRAIN_ON_MISSING", "false").lower() in ("1", "true", "yes")
