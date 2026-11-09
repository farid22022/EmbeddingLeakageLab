"""Consistent standard-library logging setup."""

import logging
import os


def configure_logging(level: str | None = None) -> None:
    """Configure root logging, defaulting to ELL_LOG_LEVEL or INFO."""
    selected = (level or os.getenv("ELL_LOG_LEVEL", "INFO")).upper()
    numeric_level = getattr(logging, selected, None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Unknown log level: {selected}")
    logging.basicConfig(level=numeric_level, format="%(levelname)s %(name)s: %(message)s")
