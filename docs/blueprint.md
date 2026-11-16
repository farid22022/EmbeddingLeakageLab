# EmbeddingLeakageLab Research and Technical Blueprint

**Status:** Phase 0 and Phase 1 are prepared for review but not gate-approved.
**Last reviewed:** 2026-11-16.
**Source of truth:** This document controls research scope and technical design.

## 1. Research purpose

Study what text information can be reconstructed or inferred from sentence
embeddings under explicit attacker access assumptions. Candidate comparisons are
Bengali script (BN), Romanized Bangla (ROM), English (EN), and Bangla-English
code-switching (MIX), using aligned fictional synthetic content. The project
has not run an inversion experiment.

## 2. Evidence status and novelty boundary

Embedding leakage has been studied since Song and Raghunathan (2020), including
partial word recovery, attribute inference, membership inference, and
defenses. Later work established generative and iterative sentence inversion
(GEIA and Vec2Text), multilingual and cross-script attacks, attacks without
victim-model queries (transferable inversion), few-shot cross-model alignment
(ALGEN), reproducibility analysis, and privacy-utility defenses (including
SPARSE). These are established prior contributions, not project claims.

The 2024 multilingual ACL study tests English, French, German, and Spanish.
The separate 2024 cross-script study enumerates 20 languages including Hindi,
Gujarati, Punjabi, Urdu, and Sinhala, but not Bengali. It reports higher
vulnerability for Indo-Aryan languages and used substantial compute. The
reviewed ALGEN paper tests English, French, German, and Spanish. These findings
verify non-inclusion in the named evaluations only; they do not prove no other
prior study covers Bengali, Romanized Bangla, or Bangla-English code-switching.
Romanized Bangla and code-mix datasets now exist, but their purpose is
transliteration, language tagging, or sentiment—not embedding inversion.

Therefore the defensible candidate contribution is a controlled,
resource-aware evaluation of Bengali-related scripts and code-switching,
outcomes, and data/access budgets under reproducible, matched conditions. It is
not “the first multilingual,” “the first Indo-Aryan,” or “the first Bengali
privacy” work. A systematic search through 2026 found no directly matching
Bangla embedding-inversion experiment within the sources logged here; this
remains a bounded review result and requires human review before any novelty
claim.

## 3. Research questions and outcomes

See [research_questions.md](research_questions.md). The provisional RQs
separate exact text, semantic propositions, fictional entity recovery,
fictional attribute inference, and later privacy-utility analysis. Each is
reported separately; no expected language ranking is assumed.

## 4. Threat model

See [experimental_protocol.md](experimental_protocol.md) for independent axes
covering victim-model queries, model identity, weights/gradients, auxiliary
paired examples, data budgets, attack pretraining, objective, and defender.
Initial future pilot candidate: known victim model, black-box weights,
explicit query access only for synthetic attacker data/hypotheses, no real
data, and separate budgets of 0/16/64 pairs. A no-query transfer threat model
is distinct and out of the first pilot. White-box evaluation is out of initial
scope.

## 5. Data and comparison design

Use 64 synthetic fictional records derived from 16 templates. Review four
aligned renderings (BN, ROM, EN, MIX) for semantic equivalence and language/script
labels. Preserve raw text and all transformed versions separately. Split by
template before rendering; keep every paraphrase and condition from one
template in one split. Use token-level tags for MIX, record whitespace and
subword token counts, and report source lineage and exclusions. Natural corpora
are candidates for later phases only after licensing, provenance, privacy, and
label-quality review.

## 6. Pilot feasibility

Owner-provided planning hardware is Intel i5-1135G7, 12 GB RAM, NVIDIA MX450
2 GB, and Intel Iris Xe; these specifications are not independently verified.
The current software runtime reports CPU and no CUDA. Future pilot defaults:
one cached, approved Bangla-capable encoder, CPU-first, batch size 4 (reduce to
1), max 128 subword tokens, one process, sequential conditions, and no large
checkpoint downloads. Establish model footprint first; warn at 2 GB process
RAM, stop at 5 GB, and record peak memory and timings. Exact model selection is
open because model identity, license, compatibility, and cache availability
must be checked before use. No attack or defense implementation is approved.

## 7. Architecture and reproducibility

The current milestone is documentation, CLI, YAML loading, seed/device/logging
helpers, and tests. Heavy ML dependencies remain optional. Later phases may add
dataset manifests, embedding adapters, attack/defense interfaces, evaluation,
immutable experiment records, and reports only after required gates.

Each future experiment requires a unique immutable ID, frozen config, data
version/checksum, model/tokenizer revisions, seed, hardware/software versions,
timestamps, metrics, runtime/memory, errors/warnings, and status. Never
overwrite completed output. Raw or sensitive text, checkpoints, caches, and
reconstructions stay out of Git.

## 8. Ethics and claim discipline

Use fictional data in development. Do not target real people or publish
recovered identifying details. Respect dataset terms. Do not send sensitive
text to external services. Label prior findings, hypotheses, and future results
separately. Do not claim novelty, significance, or performance without
verifiable evidence.

## 9. Phase 0 and Phase 1 review decisions

1. Confirm the bounded literature search and the proposed novelty language.
2. Approve or revise the four provisional RQs and the synthetic data plan.
3. Select a cached, appropriately licensed, Bangla-capable model only after its
   resource footprint and representation recipe are verified.
4. Decide whether the query-access synthetic pilot is acceptable before any
   attack implementation phase begins.
5. Resolve remaining Phase 1 evidence: Ruff and full dev-extra installation,
   Python 3.11 runtime, CI execution, and owner-approved hardware inventory.

Neither gate is complete in this revision; see `roadmap.md` and the two gate
reports. No phase advances automatically.
