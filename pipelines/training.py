from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from config.settings import MODEL_PATH
from pipelines.evaluation import evaluate_model
from pipelines.ingestion import load_dataset
from pipelines.preprocessing import FEATURE_COLUMNS, get_feature_matrix, get_target_vector, prepare_data
from pipelines.serialization import save_model
from utils.logger import configure_logger

logger = configure_logger(__name__)


def build_candidate_pipelines() -> dict:
    numeric_columns = [col for col in FEATURE_COLUMNS if col not in ["location"]]
    categorical_columns = ["location"]

    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown="ignore")

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_columns),
            ("cat", categorical_transformer, categorical_columns),
        ]
    )

    return {
        "LinearRegression": Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("model", LinearRegression()),
            ]
        ),
        "RandomForest": Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("model", RandomForestRegressor(n_estimators=150, random_state=42)),
            ]
        ),
    }


def compare_models(X_train, X_test, y_train, y_test):
    candidates = build_candidate_pipelines()
    results = []
    best_result = {"r2": float("-inf")}
    best_pipeline = None
    best_name = None

    for name, pipeline in candidates.items():
        logger.info("Training candidate model: %s", name)
        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)
        metrics = evaluate_model(y_test, y_pred)
        metrics["model"] = name
        results.append(metrics)
        logger.info("%s metrics: %s", name, metrics)

        if metrics["r2"] > best_result["r2"]:
            best_result = metrics
            best_pipeline = pipeline
            best_name = name

    return best_name, best_pipeline, results


def run_training_pipeline(data_path: Path | str | None = None, model_path: Path | str | None = None):
    df = load_dataset(data_path)
    X, y = prepare_data(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    best_name, best_pipeline, results = compare_models(X_train, X_test, y_train, y_test)
    logger.info("Selected best model: %s", best_name)

    bundle = {
        "model": best_pipeline,
        "metadata": {
            "name": best_name,
            "feature_columns": FEATURE_COLUMNS,
        },
    }

    saved_path = save_model(bundle, model_path)
    logger.info("Saved best model to %s", saved_path)
    return saved_path, results
