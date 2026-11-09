"""Small, safe YAML configuration loader."""

from pathlib import Path
from typing import Any

import yaml


def load_yaml(path: str | Path) -> dict[str, Any]:
    """Load a YAML mapping and reject empty or non-mapping documents."""
    config_path = Path(path)
    try:
        with config_path.open(encoding="utf-8") as stream:
            value = yaml.safe_load(stream)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Configuration file not found: {config_path}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"Configuration must be a YAML mapping: {config_path}")
    return value
