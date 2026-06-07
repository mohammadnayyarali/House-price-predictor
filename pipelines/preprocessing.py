from typing import Tuple
import pandas as pd

FEATURE_COLUMNS = [
    "area",
    "bedrooms",
    "bathrooms",
    "age",
    "bed_bath_ratio",
    "garage",
    "lot_size",
    "location",
]


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.dropna()
    df = df[df["area"] > 0]
    df = df[df["price"] > 0]
    df["location"] = df["location"].astype(str).str.strip()
    return df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["age"] = 2026 - df["year_built"]
    df["bed_bath_ratio"] = df["bedrooms"] / df["bathrooms"].replace(0, 1)
    return df


def get_feature_matrix(df: pd.DataFrame) -> pd.DataFrame:
    return df[FEATURE_COLUMNS].copy()


def get_target_vector(df: pd.DataFrame) -> pd.Series:
    return df["price"].copy()


def prepare_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    df = clean_data(df)
    df = engineer_features(df)
    X = get_feature_matrix(df)
    y = get_target_vector(df)
    return X, y
