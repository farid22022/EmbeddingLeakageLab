# EmbeddingLeakageLab

**A reproducible research framework for studying privacy leakage from Bangla
and multilingual text embeddings.**

EmbeddingLeakageLab is an early-stage research engineering project. It is
designed to make data provenance, attacker assumptions, model choices,
experiments, and limitations visible and reproducible. Its planned scope covers
Bangla script, Romanized Bangla, English, and Bangla-English code-switched text.

> **Current status:** Phase 0 (research foundation) and Phase 1 (repository
> foundation) are in progress. The starter CLI and foundation tests exist.
> Dataset pipelines, embedding generation, inversion attacks, privacy defenses,
> and empirical results have not been implemented. The proposed research gap is
> preliminary; this repository makes no novelty or performance claim.

## Research objectives

The long-term project aims to support a reproducible research lifecycle:

1. Review prior work and state a defensible research gap.
2. Define research questions, hypotheses, and attacker threat models.
3. Prepare provenance-tracked, split-safe multilingual datasets.
4. Generate embeddings with documented model and tokenizer revisions.
5. Compare text reconstruction, retrieval, entity recovery, and attribute
   inference attacks as distinct tasks.
6. Evaluate privacy defenses alongside downstream utility.
7. Record experiments immutably and produce traceable reports.

The project does not treat these aims as completed capabilities. Work advances
through the gates documented in the [roadmap](roadmap.md).

## Research scope

### Language and script conditions

| Label | Condition |
|---|---|
| BN | Bangla in Bangla script |
| ROM | Romanized Bangla |
| EN | English |
| MIX | Bangla-English code-switched text |

Initial sentence-length categories are short (5–10 tokens), medium (11–25), and
long (26–50). The tokenizer and counting rules must be documented before
experiments; these categories are configurable design targets, not results.

### Provisional research questions

- How much text and sensitive information can be recovered from embeddings
  under clearly stated attacker access assumptions?
- How does leakage vary across BN, ROM, EN, and MIX?
- How do encoder architecture, sentence length, language, and script affect
  reconstruction and inference?
- Can entities or attributes be recovered when exact text reconstruction fails?
- How do selected privacy transformations affect leakage and legitimate utility?

These questions and their hypotheses are tracked in
[docs/research_questions.md](docs/research_questions.md). They are not findings.

## Prior work and research positioning

Embedding inversion is an established research area. Vec2Text introduced
iterative text reconstruction from dense embeddings; GEIA studied generative
reconstruction; later work investigated multilingual and cross-lingual attacks,
transfer attacks without victim-model queries, script/language confusion, and
few-shot cross-model alignment. Bangla sentence embedding models also exist.
Accordingly, “multilingual inversion” alone is not a novelty claim for this
project. Whether the exact BN, ROM, and MIX conditions are adequately covered by
prior evaluations remains under review.

The [literature review](literature_review/index.md) and
[verification log](literature_review/verification_log.md) record what has been
checked and what remains uncertain. The candidate focus is a controlled,
resource-aware comparison of Bangla script, Romanized Bangla, and code-switching
with explicit model compatibility, threat-model, and privacy–utility controls.
That candidate gap must be verified against full papers and appendices before
it is presented as a contribution.

## Project status and phase gates

| Phase | Focus | Status |
|---|---|---|
| 0 | Literature review, research gap, threat model, and protocol | In progress; Gate 0 not ready |
| 1 | Python package, documentation, CLI, and development setup | In progress; Gate 1 not ready |
| 2 | Dataset engineering | Not started |
| 3 | Embedding generation | Not started |
| 4 | Baseline leakage evaluation | Not started |
| 5 | Embedding inversion attacks | Not started |
| 6 | Privacy defenses | Not started |
| 7 | Comparative multilingual experiments | Not started |
| 8 | Robustness and error analysis | Not started |
| 9 | Final evaluation and artifact freeze | Not started |
| 10 | Research paper and release preparation | Not started |

The [roadmap](roadmap.md) is the progress record. A phase is complete only when
its implementation and verification criteria pass. The CLI does not advance
phases automatically.

## Repository structure

```text
EmbeddingLeakageLab/
├── AGENTS.md                    # Permanent instructions for coding agents
├── README.md                    # Project overview and getting started
├── roadmap.md                   # Phase checklist, progress, and gates
├── CHANGELOG.md                 # Project change history
├── pyproject.toml               # Python package and tool configuration
├── .github/workflows/tests.yml  # Windows CI test workflow
├── docs/
│   ├── blueprint.md             # Research and technical design source of truth
│   ├── experimental_protocol.md # Provisional protocol for Gate 0 review
│   ├── research_questions.md    # Questions and hypotheses
│   ├── methodology.md           # Comparison and analysis constraints
│   ├── reproducibility.md       # Experiment record requirements
│   ├── ethics.md                # Data and publication safeguards
│   └── setup.md                 # Installation and CLI instructions
├── literature_review/
│   ├── index.md                 # Starting literature review and gap map
│   ├── research_gap.md          # Preliminary gap assessment
│   ├── comparison_matrix.csv    # Paper comparison records
│   └── verification_log.md      # Metadata checks and open questions
├── src/embedding_leakage/
│   ├── core/                    # YAML, seed, device, and logging helpers
│   └── cli/                     # Initial research progress CLI
└── tests/                       # Foundation and CLI unit tests
```

The later-phase architecture is described in
[docs/architecture.md](docs/architecture.md). Modules are added as phases
require them; unimplemented features are not represented as working code.

## Quick start

### Requirements

- Python 3.11 or newer.
- Windows PowerShell for the commands below; other platforms may work but are
  not currently the CI target.

The starter package depends on PyYAML. The development extra includes pytest
and Ruff. PyTorch and Transformers are optional for the current CLI; no model
downloads or inference are required.

### Install

```powershell
git clone https://github.com/farid22022/EmbeddingLeakageLab.git
cd EmbeddingLeakageLab
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If PowerShell blocks activation, use the Python executable directly:

```powershell
.venv\Scripts\python.exe -m pip install -e ".[dev]"
```

### Run the starter checks and CLI

```powershell
pytest -q
ruff check .
ell --help
ell status
ell roadmap
ell phase show 0
ell phase next
ell doctor
```

Available CLI commands are currently limited to progress inspection and the
environment report. Data, model, embedding, experiment, and reporting commands
listed in the research plan have not been implemented yet.

## Reproducibility principles

Every future experiment must record a unique ID, dataset version and checksum,
model/tokenizer/attack revisions, immutable configuration and hash, seed,
hardware and software environment, execution times, metrics, runtime, memory,
warnings, errors, and status transitions. Completed results must not be
overwritten. Reports must identify whether a result is preliminary or
confirmatory and link claims to their experiment artifacts.

Raw datasets, checkpoints, caches, credentials, and sensitive reconstructions
must stay out of Git. Small manifests and research reports may be tracked when
they contain no private data. See [docs/reproducibility.md](docs/reproducibility.md)
and the [ethical data guidance](docs/ethics.md).

## Ethics and responsible research

- Prefer fictional synthetic personal data for development and pilot work.
- Do not target real individuals or publish recovered personal information.
- Do not send sensitive text or reconstructions to external services without
  explicit authorization.
- Record data provenance and respect dataset licenses and terms.
- Do not put credentials in source code, logs, manifests, or reports.
- Report privacy risks, failed runs, and limitations transparently.

See [SECURITY.md](SECURITY.md) and [docs/ethics.md](docs/ethics.md).

## Contributing and development workflow

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md) before
changing the project. Work on the active roadmap phase, add focused tests, and
update the roadmap, relevant documentation, and changelog with completed work.
Use short-lived branches for changes and meaningful, scoped commit messages,
such as `docs: clarify multilingual research scope` or
`feat: add dataset validation`. Do not mark a phase complete or begin the next
phase automatically; phase gates require human review.

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE).

## Acknowledgments and references

The project organization takes inspiration from the public
[IntentGate repository](https://github.com/Atik203/IntentGate); its code is not
used as the implementation for this project. The literature review links to
primary paper records, including:

- Morris et al. (2023), [Text Embeddings Reveal (Almost) As Much As Text](https://aclanthology.org/2023.emnlp-main.765/).
- Li et al. (2023), [Generative Embedding Inversion Attack (GEIA)](https://aclanthology.org/2023.findings-acl.881/).
- Chen et al. (2024), [Text Embedding Inversion Security for Multilingual Language Models](https://aclanthology.org/2024.acl-long.422/).
- Chen et al. (2024), [Against All Odds: multilingual embedding inversion across typology and scripts](https://arxiv.org/abs/2408.11749).
- Chen et al. (2025), [ALGEN: Few-shot Inversion Attacks](https://aclanthology.org/2025.acl-long.1185/).

See [literature_review/index.md](literature_review/index.md) for the scope and
verification status of these records.
