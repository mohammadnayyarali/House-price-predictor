from pathlib import Path
import pandas as pd

from config.settings import DATA_PATH
from utils.file_utils import ensure_file_exists

REQUIRED_COLUMNS = {
    "area",
    "bedrooms",
    "bathrooms",
    "year_built",
    "garage",
    "lot_size",
    "location",
    "price",
}


def load_dataset(data_path: str | Path | None = None) -> pd.DataFrame:
    path = Path(data_path or DATA_PATH)
    ensure_file_exists(path)
    df = pd.read_csv(path)
    missing_columns = REQUIRED_COLUMNS - set(df.columns)
    if missing_columns:
        raise ValueError(f"Data is missing required columns: {sorted(missing_columns)}")
    return df
