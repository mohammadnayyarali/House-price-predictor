import pandas as pd

DATA_PATH = "data/house_prices_sample.csv"

LOCATION_MAP = {
    "Downtown": 0,
    "Suburb": 1,
    "Uptown": 2,
}


def load_data(path: str = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna().copy()
    df = df[df["area"] > 0]
    df = df[df["price"] > 0]
    df["location"] = df["location"].astype(str).str.strip().replace({"Downtown": "Downtown", "Suburb": "Suburb", "Uptown": "Uptown"})
    return df


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["age"] = 2026 - df["year_built"]
    df["bed_bath_ratio"] = df["bedrooms"] / df["bathrooms"].replace(0, 1)
    return df


def prepare_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    return df[["area", "bedrooms", "bathrooms", "age", "bed_bath_ratio", "garage", "lot_size", "location"]]


def prepare_target(df: pd.DataFrame) -> pd.Series:
    return df["price"]
