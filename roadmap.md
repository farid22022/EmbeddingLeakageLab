# Research Roadmap

## Current Status

Current Phase: 0
Overall Status: PLANNING
Last Updated: 2026-11-16

- **Completed phases:** None.
- **Current active task:** Human review of the prepared Phase 0 and Phase 1
  gate reports; complete the bounded literature matrix and outstanding Phase 1
  verification before phase advancement.
- **Pending tasks:** Complete remaining full-paper extraction and confirm a
  feasible cached Bangla-capable encoder; run Ruff/dev extras and supported
  Python/Windows CI; verify physical hardware inventory if available.
- **Blocked tasks:** Ruff/dev-extra install is blocked by unavailable package
  index DNS/network; Python 3.11 and remote CI were not run; hardware inventory
  is not independently verified.
- **Phase completion:** Phase 0 = 82%; Phase 1 = 80%; overall = N/A until later
  phase checklists are decomposed into measurable tasks.
- **Latest successful experiment:** None.
- **Latest failed experiment:** None.
- **Outstanding issues:** Gate 0 matrix has NOT REPORTED fields and is not an
  exhaustive review; candidate encoder artifact/license/resource footprint
  needs verification. Gate 1 still lacks Ruff, Python 3.11, remote CI and full
  inventory evidence.
- **Next recommended task:** Review and approve the proposed research questions,
  threat model and protocol, then complete remaining gate evidence. Do not
  advance phases automatically.

## Phase Overview

| Phase | Name | Status | Completion |
|-------|------|--------|------------|
| 0 | Literature Review | IN PROGRESS | 50% |
| 1 | Repository Foundation | IN PROGRESS | 70% |
| 2 | Dataset Engineering | TODO | 0% |
| 3 | Embedding Engine | TODO | 0% |
| 4 | Baseline Evaluation | TODO | 0% |
| 5 | Inversion Attacks | TODO | 0% |
| 6 | Privacy Defences | TODO | 0% |
| 7 | Comparative Experiments | TODO | 0% |
| 8 | Robustness Analysis | TODO | 0% |
| 9 | Final Evaluation | TODO | 0% |
| 10 | Research Release | TODO | 0% |

Percentages are computed from the checklist items below (completed items divided
by all non-deferred items; in-progress items do not count as complete).

## Phase 0 — Research Foundation and Literature Review

**Goal:** Establish prior work, research gap, questions, and a feasible threat
model before attack implementation.

- [x] Inspect repository and reference IntentGate organization.
- [x] Verify core Vec2Text, GEIA, multilingual, transfer, and Bangla embedding
  paper metadata from primary records.
- [x] Download and register the six user-prioritized core papers with source,
  license, and checksum records.
- [x] Create initial research questions and hypothesis document.
- [x] Record preliminary novelty boundary and methodological risks.
- [x] Review the full language list, dataset scale, models, access setup and
  resource limits in the closest 2024 cross-script paper.
- [x] Search 2025–2026 primary papers and Bangla Romanized/code-mix resources;
  document the structured search scope and limitations.
- [~] Complete literature comparison matrix with datasets, models, metrics,
  findings, limitations, and relevance for each paper.
- [x] Prepare bounded research-gap assessment without a global novelty claim.
- [x] Prepare provisional threat model and feasibility-reviewed protocol.
- [ ] Human review of remaining extraction gaps, candidate model/license/resource
  footprint, RQs, threat model, and protocol.

**Deliverables:** Gate 0 documents, expanded matrix, bibliography, and gate
report are prepared; detailed extraction and approval remain open.

**Gate 0 status:** READY FOR HUMAN REVIEW; NOT COMPLETE. Do not implement full
attacks before remaining review tasks are complete and reviewed. See
[`docs/phase0_gate_report.md`](docs/phase0_gate_report.md).

## Phase 1 — Repository Foundation and Environment

**Goal:** Establish the starter project, progress CLI, and basic environment
helpers.

- [x] Initialize package metadata and repository documentation.
- [x] Add ignore rules for credentials, datasets, weights, caches, and results.
- [x] Implement YAML loading, seed setup, device detection, and logging helpers.
- [x] Implement initial status, roadmap, phase, and doctor CLI commands.
- [x] Add focused unit tests for foundation helpers and CLI behavior.
- [x] Install project editable and verify installed CLI command (Python 3.12;
  Ruff/dev extras remain blocked by unavailable package index).
- [x] Add initial Windows CI workflow for Python 3.11 and 3.12.
- [ ] Complete setup and installation checks in CI.
- [~] Collect system hardware details: runtime reports CPU/no CUDA; physical
  CPU/RAM/GPU inventory remains owner-provided and unverified.
- [x] Complete project README with scope, setup, status, governance, and
  literature positioning.

**Deliverables:** Starter package, CLI, setup guide, tests, and progress tracker.

**Verification evidence:** Editable install succeeded; installed CLI version,
status, roadmap, phase-next, and doctor commands succeeded; `pytest -q` passed
(10 tests, Python 3.12.7). Ruff installation was blocked by package-index DNS;
Ruff, Python 3.11, dev-extra install, and remote Windows CI were not run. See
[`docs/phase1_verification_report.md`](docs/phase1_verification_report.md).

**Gate 1 status:** READY FOR HUMAN REVIEW; NOT COMPLETE because lint, Python
3.11, remote CI, and physical inventory evidence are missing. No phase
transition occurs automatically.

## Phases 2–10

See the master project prompt and `docs/blueprint.md` for objectives and gate
requirements. These phases remain TODO and must be designed/implemented only as
their dependencies and explicit phase approval permit.
