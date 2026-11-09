# Research Roadmap

## Current Status

Current Phase: 0
Overall Status: PLANNING
Last Updated: 2026-11-10

- **Completed phases:** None.
- **Current active task:** Extract methods, language coverage, datasets, models,
  and metrics from the 2024–2026 inversion and defense papers.
- **Pending tasks:** Complete Gate 0 literature and protocol review; complete
  Phase 1 editable-install, CI, and hardware checks.
- **Blocked tasks:** Hardware inventory query unavailable in the current
  environment.
- **Phase completion:** Phase 0 = 50%; Phase 1 = 70%; overall = N/A until later
  phase checklists are decomposed into measurable tasks.
- **Latest successful experiment:** None.
- **Latest failed experiment:** None.
- **Outstanding issues:** Complete systematic 2023–2026 literature audit;
  verify Bangla/ROM/MIX coverage; finalize feasible pilot and primary metrics.
- **Next recommended task:** Extract language/model/dataset/threat details from
  the full text and appendices of the closest multilingual inversion papers.

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
- [~] Review full methods and appendices, including language coverage.
- [ ] Search and verify relevant 2026 primary research.
- [ ] Complete literature comparison matrix with datasets, models, metrics,
  findings, limitations, and relevance for each paper.
- [ ] Finalize research gap based on verified coverage.
- [ ] Finalize threat model and feasibility-reviewed protocol.

**Deliverables:** Initial versions of all Gate 0 documents exist; the literature
set and gap are explicitly preliminary.

**Gate 0 status:** NOT READY. Do not implement full attacks before remaining
review tasks are complete and reviewed.

## Phase 1 — Repository Foundation and Environment

**Goal:** Establish the starter project, progress CLI, and basic environment
helpers.

- [x] Initialize package metadata and repository documentation.
- [x] Add ignore rules for credentials, datasets, weights, caches, and results.
- [x] Implement YAML loading, seed setup, device detection, and logging helpers.
- [x] Implement initial status, roadmap, phase, and doctor CLI commands.
- [x] Add focused unit tests for foundation helpers and CLI behavior.
- [ ] Install project with development extras and verify editable CLI command.
- [x] Add initial Windows CI workflow for Python 3.11 and 3.12.
- [ ] Complete setup and installation checks in CI.
- [ ] Collect system hardware details through a permitted local environment
  query; current hardware numbers are provided by the project prompt only.
- [x] Complete project README with scope, setup, status, governance, and
  literature positioning.

**Deliverables:** Starter package, CLI, setup guide, tests, and progress tracker.

**Verification evidence:** `python -m pytest -q` passed (10 tests); CLI status,
roadmap, and doctor smoke commands completed. Ruff is not installed locally, and
the editable package installation/CI workflow have not been run. The hardware
inventory command was blocked in this environment.

**Gate 1 status:** NOT READY FOR REVIEW. No phase transition occurs
automatically.

## Phases 2–10

See the master project prompt and `docs/blueprint.md` for objectives and gate
requirements. These phases remain TODO and must be designed/implemented only as
their dependencies and explicit phase approval permit.
