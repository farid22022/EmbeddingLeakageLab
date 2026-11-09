# Instructions for coding agents

## Authoritative project records

- `docs/blueprint.md` is the research and technical design source of truth.
- `roadmap.md` tracks phase tasks, measured progress, blockers, and gates.
- `AGENTS.md` contains permanent contribution instructions.
- If these disagree, stop to record the conflict and resolve it explicitly; do
  not silently choose one.

## Before making changes

1. Read this file, `roadmap.md`, the relevant blueprint section, and affected
   source files.
2. Inspect `git status` and preserve user changes and completed experiment data.
3. Confirm the active phase and select its next incomplete checklist item.
4. Check whether the paper or implementation facts are current and primary
   sourced before recording research claims.

## Implementation rules

- Work only in the active phase unless a dependency requires otherwise.
- Do not create misleading placeholders or fabricated results.
- Preserve original text alongside any normalized or transformed text.
- Prefer synthetic personal data. Do not target real people or publish recovered
  personal information.
- Do not send sensitive text to external services without explicit authorization.
- Keep credentials, raw data, model checkpoints, caches, and sensitive outputs
  out of Git.
- Every experiment needs an immutable unique ID and enough version/configuration
  metadata to reproduce it. Never overwrite completed results.
- Record deviations and limitations in the blueprint or experiment report.
- Update `roadmap.md`, relevant docs, and `CHANGELOG.md` together when a task is
  completed.

## Verification and gates

- Add focused automated tests with each implementation task.
- Run the relevant checks and report exact outcomes; do not claim unrun checks.
- A phase is complete only when its implementation, verification, acceptance
  criteria, and gate evidence are satisfied.
- Never advance a phase automatically. After preparing a gate report and marking
  it READY FOR REVIEW, wait for explicit human approval before advancing.
- Do not claim novelty, statistical significance, or performance without
  verifiable evidence.
