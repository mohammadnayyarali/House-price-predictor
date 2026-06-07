from pathlib import Path

from pipelines.training import run_training_pipeline
from utils.logger import configure_logger

logger = configure_logger(__name__)


def main(data_path: Path | str | None = None, model_path: Path | str | None = None):
    saved_path, results = run_training_pipeline(data_path=data_path, model_path=model_path)
    logger.info("Training completed. Model saved to %s", saved_path)
    for metrics in results:
        logger.info("Model evaluation: %s", metrics)


if __name__ == "__main__":
    main()
