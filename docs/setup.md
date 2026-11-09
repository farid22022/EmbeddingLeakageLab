# Setup

## Requirements

Python 3.11 or newer. This repository currently uses Python 3.12 in the
development environment. The first milestone needs PyYAML; development checks
use pytest and Ruff. PyTorch/Transformers are not imported by the starter CLI.

## Install

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
pytest -q
ruff check .
ell --help
ell doctor
```

The current environment already has pytest, PyYAML, NumPy, Pandas, PyTorch and
Transformers; Ruff is not installed. The machine's hardware query was not
available in this execution context. The hardware figures in the blueprint are
provided in the project brief and have not been independently checked.

## CLI

The initial CLI supports `ell status`, `ell roadmap`, `ell phase show N`,
`ell phase next`, and `ell doctor`. Research commands are added incrementally;
the CLI does not automatically advance phases.
