import logging

from config.settings import LOG_LEVEL


def configure_logger(name: str = "house_price_app", level: str | int | None = None):
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    resolved_level = level or LOG_LEVEL
    if isinstance(resolved_level, str):
        resolved_level = resolved_level.upper()

    logger.setLevel(resolved_level)
    return logger
