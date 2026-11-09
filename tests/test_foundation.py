import sys
from pathlib import Path
from types import ModuleType, SimpleNamespace

import pytest

from embedding_leakage.core.config import load_yaml
from embedding_leakage.core.device import detect_device
from embedding_leakage.core.logger import configure_logging
from embedding_leakage.core.seed import set_seed


def test_load_yaml_mapping(tmp_path: Path) -> None:
    config_file = tmp_path / "config.yaml"
    config_file.write_text("seed: 7\nname: pilot\n", encoding="utf-8")

    assert load_yaml(config_file) == {"seed": 7, "name": "pilot"}


def test_load_yaml_rejects_non_mapping(tmp_path: Path) -> None:
    config_file = tmp_path / "config.yaml"
    config_file.write_text("- value\n", encoding="utf-8")

    with pytest.raises(ValueError, match="mapping"):
        load_yaml(config_file)


def test_seed_is_repeatable_for_python(monkeypatch) -> None:
    import random

    fake_torch = ModuleType("torch")
    fake_torch.manual_seed = lambda seed: None
    fake_torch.cuda = SimpleNamespace(is_available=lambda: False)
    monkeypatch.setitem(sys.modules, "torch", fake_torch)

    set_seed(123)
    first = random.random()
    set_seed(123)

    assert random.random() == first


def test_device_detection_returns_info(monkeypatch) -> None:
    fake_torch = ModuleType("torch")
    fake_torch.cuda = SimpleNamespace(is_available=lambda: False)
    monkeypatch.setitem(sys.modules, "torch", fake_torch)

    info = detect_device()

    assert info.name in {"cpu", "cuda"}
    assert isinstance(info.cuda_available, bool)


def test_logger_rejects_unknown_level() -> None:
    with pytest.raises(ValueError, match="Unknown log level"):
        configure_logging("not-a-level")
