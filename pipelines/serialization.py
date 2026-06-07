from pathlib import Path
import joblib

from config.settings import MODEL_PATH
from utils.file_utils import ensure_directory


def save_model(bundle: dict, model_path: Path | str | None = None) -> Path:
    path = Path(model_path or MODEL_PATH)
    ensure_directory(path.parent)
    joblib.dump(bundle, path)
    return path


def load_model(model_path: Path | str | None = None) -> dict:
    path = Path(model_path or MODEL_PATH)
    if not path.exists():
        raise FileNotFoundError(f"Serialized model not found at {path}")
    return joblib.load(path)
