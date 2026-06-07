from pathlib import Path


def ensure_directory(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def ensure_file_exists(path: Path):
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")
    return path


def ensure_path_is_writable(path: Path) -> Path:
    if path.exists() and not path.is_file():
        raise FileExistsError(f"Expected file path, found directory: {path}")
    ensure_directory(path.parent)
    return path
