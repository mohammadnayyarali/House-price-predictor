from pathlib import Path
from typing import Optional

import pandas as pd

from config import settings
from pipelines.serialization import load_model
from pipelines.training import run_training_pipeline
from utils.logger import configure_logger

logger = configure_logger(__name__)


class Predictor:
    def __init__(self, model_path: Optional[str] = None, auto_train: Optional[bool] = None):
        self.model_path = Path(model_path or settings.MODEL_PATH)
        self.auto_train = settings.AUTO_TRAIN_ON_MISSING if auto_train is None else auto_train
        self.pipeline = None
        self.metadata = {}
        self._initialize_model()

    def _initialize_model(self):
        if self.model_path.exists():
            self._load_model()
            return

        if self.auto_train:
            logger.warning("Model not found at %s. Auto-training enabled.", self.model_path)
            self._train_model()
            return

        logger.warning("Model missing at %s and AUTO_TRAIN_ON_MISSING=false.", self.model_path)

    def _load_model(self):
        bundle = load_model(self.model_path)
        self.pipeline = bundle["model"]
        self.metadata = bundle.get("metadata", {})
        logger.info("Loaded model from %s", self.model_path)

    def _train_model(self):
        saved_path, _ = run_training_pipeline(model_path=self.model_path)
        self._load_model()
        logger.info("Auto-trained model saved to %s", saved_path)

    def _prepare_input(self, payload) -> pd.DataFrame:
        age = 2026 - payload.year_built
        bed_bath_ratio = payload.bedrooms / payload.bathrooms if payload.bathrooms != 0 else float(payload.bedrooms)
        row = {
            "area": [payload.area],
            "bedrooms": [payload.bedrooms],
            "bathrooms": [payload.bathrooms],
            "age": [age],
            "bed_bath_ratio": [bed_bath_ratio],
            "garage": [payload.garage],
            "lot_size": [payload.lot_size],
            "location": [payload.location],
        }
        return pd.DataFrame(row)

    def predict(self, payload) -> float:
        if self.pipeline is None:
            raise FileNotFoundError(
                f"Model file not found at {self.model_path}. "
                "Run the training pipeline or set AUTO_TRAIN_ON_MISSING=true."
            )

        features = self._prepare_input(payload)
        prediction = self.pipeline.predict(features)
        return float(round(prediction[0], 2))
