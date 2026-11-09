# Experimental protocol (provisional)

**Status:** Draft for Gate 0 review; not an executable experiment plan.

## Purpose

Compare embedding leakage across Bangla script (BN), Romanized Bangla (ROM),
English (EN), and Bangla-English code-switching (MIX) while separating text
reconstruction, semantic reconstruction, entity recovery, and attribute
inference. These conditions and outcomes are not assumed to be directly
comparable without source and semantic controls.

## Required controls before confirmatory experiments

- Define attacker access per attack: victim model queries, model identity,
  auxiliary paired examples, leaked embedding count, and training corpus.
- Pin dataset version, provenance, source-level split, and checksum.
- Keep source text and transformed/normalized text in separate fields.
- Document tokenization, language/script labeling, transliteration, code-switch
  rules, and length counting.
- Use paired source samples where feasible; record translation/transliteration
  edits and validate meaning equivalence.
- Pin embedding model and tokenizer revisions, architecture, pooling, prompts,
  normalization, dimensions, and license.
- Use fixed seeds and identical evaluation code across language conditions.
- Preserve failed, missing, incompatible, and resource-limited runs with their
  status and error context.

## Metrics and analysis

Choose exact string, character/word error, semantic, entity, attribute, and
downstream utility metrics separately for the relevant outcome. Before
confirmatory work, define confidence intervals, paired tests, effect sizes, and
multiple-comparison handling. Never treat a membership inference score or
retrieval success as an inversion score.

## Feasibility and ethics

Start with fictional synthetic examples and small CPU-capable pilots. No large
datasets/checkpoints or external APIs are authorized by this draft. Keep
personal data and sensitive reconstructions out of tracked artifacts. Final
sample sizes, model list, resource budget, and threat model are Gate 0 decisions.
