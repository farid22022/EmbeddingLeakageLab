# EmbeddingLeakageLab Research and Technical Blueprint

**Status:** Initial design; Phase 0 review remains open.
**Last reviewed:** 2026-11-09
**Source of truth:** This document controls research scope and technical design.

## 1. Research purpose

Measure what information an attacker can reconstruct or infer from text
embeddings under explicitly defined access assumptions, with controlled
comparisons among Bangla script (BN), Romanized Bangla (ROM), English (EN), and
Bangla-English code-switching (MIX). The target population, datasets, models,
attack assumptions, and claims remain subject to Phase 0 evidence review.

## 2. Evidence status and novelty boundary

Embedding inversion is established prior work. Vec2Text (Morris et al., 2023),
GEIA (Li et al., 2023), multilingual and cross-lingual inversion (Chen et al.,
2024), transfer attacks without victim-model queries (Huang et al., 2024), and
few-shot cross-model alignment and generation (Chen et al., 2025) all predate
this project. A 2024 study also examines typology, script, and language confusion
across 20 languages, reporting elevated risk for Indo-Aryan languages. Seputis
et al. (2025) report a Vec2Text reproducibility study with sequence-length and
quantization analyses. Tsai et al. (2026) introduce SPARSE, a concept-aware
defense using learned sensitive-dimension masks and Mahalanobis noise.

Therefore, “multilingual inversion” is not a defensible novelty claim. Whether
Bangla itself, Romanized Bangla, and Bangla-English code-switching are covered
in earlier experimental language lists has not yet been conclusively verified.
The narrow possible gap is an evidence-backed, controlled study of these
conditions, including script/transliteration and code-switching effects, model
compatibility, entity/attribute leakage, and privacy-utility tradeoffs under
current attack and defense baselines. This is a candidate gap only; it must be
checked against complete paper appendices, language lists, related work through
2026, and available Bangla datasets/models before Gate 0. A new defense is not
assumed necessary or novel.

## 3. Provisional research questions and hypotheses

See [research_questions.md](research_questions.md). RQs and hypotheses are
provisional, not established results.

## 4. Scope and threat model to resolve

The attack objective may be exact text reconstruction, semantic reconstruction,
entity recovery, or sensitive attribute inference. These are distinct outcomes
and must be reported separately. Threat-model variants must state whether an
attacker has victim-model query access, auxiliary paired data, model identity,
training data, or only leaked embeddings. Do not pool white-box, black-box,
transfer, and retrieval attacks into a single “inversion” score.

Phase 0 must decide primary and secondary threat models, attacker knowledge,
defender interface, and a feasible pilot. The hardware supplied in the project
prompt (i5-1135G7, 12 GB RAM, NVIDIA MX450 2 GB, Intel Iris Xe) is planning
context, not independently verified inventory. CPU and small pilots are the
default; no large checkpoints or expensive inference are part of this milestone.

## 5. Comparison design

Four language/script conditions are planned: BN, ROM, EN, and MIX. Initial
sentence-length bands are 5–10, 11–25, and 26–50 tokens and must be configurable.
Comparisons require explicit alignment/provenance and must account for meaning
changes from translation or transliteration. Preserve source text; store any
normalized/transliterated version separately. Define how tokenization and
language labels work for mixed text before counting lengths.

## 6. Initial architecture

The first milestone provides documentation, a small CLI, environment checks,
seed/device helpers, and progress tracking. Later phases may introduce data
loaders and manifests, embedding adapters, attack and defense interfaces,
evaluation, experiment metadata, and reports. Do not create empty modules just
to mimic the target tree. Heavy ML dependencies remain optional until a phase
actually uses them.

## 7. Reproducibility contract

Every future run must have a unique ID; immutable configuration; dataset
version/checksum; model and tokenizer revisions; seed; hardware/software
metadata; start/end timestamp; metrics; runtime/memory; warnings/errors; and
status history. A completed run must never be silently overwritten. Small
manifests/reports may be tracked; raw/private data, checkpoints, caches, and
sensitive reconstructions stay out of Git.

## 8. Ethics and claim discipline

Use fictional synthetic personal information by default. Do not target real
individuals or publish reconstructed identifying details. Respect dataset
license and provenance. Distinguish prior findings, hypotheses, pilot
observations, and confirmatory results. No result or novelty claim exists until
produced by an auditable experiment.

## 9. Phase 0 open decisions

1. Verify the full language lists and threat assumptions in 2024 multilingual
   work, including its 20-language follow-up.
2. Search 2025–2026 primary sources for Bangla-specific inversion, entity
   leakage, defenses, and code-switching studies; record the search protocol.
3. Verify source coverage for BN, ROM, EN, MIX and comparability across datasets.
4. Select a small number of embedding models based on architecture, pooling,
   tokenizer, language support, license, and availability on this hardware.
5. Finalize one feasible threat model and primary metric set before attack work.
