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

The local verification used Python 3.12.7 and a workspace-local virtual
environment with system packages available. Editable installation succeeded
using `--no-deps --no-build-isolation`; the regular development-extra install
was not completed because package-index DNS/network access was unavailable.
Ruff was therefore not installed or run. `pytest -q` passed all 10 tests.
The installed `ell` version/status/roadmap/phase/doctor commands succeeded;
doctor reports CPU and no CUDA in this Python runtime. Python 3.11 and remote
Windows CI were not run. Hardware figures in the blueprint are owner-provided
and physical inventory has not been independently verified. See
[`phase1_verification_report.md`](phase1_verification_report.md) for exact
commands and results.

On this managed Windows environment, setuptools rejected the injected system
temporary path during editable wheel creation. Retrying with `TEMP` and `TMP`
pointing to a repository-local `.tmp/` directory succeeded. That directory is
ignored by Git.

## CLI

The initial CLI supports `ell status`, `ell roadmap`, `ell phase show N`,
`ell phase next`, and `ell doctor`. Research commands are added incrementally;
the CLI does not automatically advance phases.
