# Research gap assessment (preliminary)

## Established coverage

Primary literature has already introduced iterative reconstruction (Vec2Text),
generative inversion (GEIA), multilingual/cross-lingual inversion and masking,
transfer attacks without victim-model queries, and few-shot cross-model
alignment/generation. A 2024 follow-up investigates 20 languages and 12 scripts
and reports risk among Indo-Aryan languages. A Bangla sentence-embedding model
family also exists.

## Candidate gap, not a novelty claim

A narrowly controlled evaluation of Bangla script, Romanized Bangla, and
Bangla-English code-switching across explicitly specified models, attacker
access assumptions, lengths, entity/attribute targets, and privacy-utility
controls may add useful evidence. The exact overlap with prior language lists,
datasets, and 2025–2026 papers has not yet been checked. The project must not
claim to be the first multilingual or Indo-Aryan inversion study.

## Methodological risks to resolve

1. Translation, transliteration, and code-switching can alter meaning and
   information content, making direct condition comparisons invalid.
2. Bangla text normalization and tokenization can affect exact and character
   metrics; preserve raw text and document script-specific processing.
3. Sentence encoders differ in pooling, prompts, normalization, dimensions, and
   training corpora; a model label alone does not define the embedding method.
4. Attack papers use different threat models and data budgets. Results cannot
   be compared without matched access and training controls.
5. Embedding utility tasks may be language-imbalanced or invalid as a proxy for
   legitimate use; select them based on actual use cases and data.
6. Small hardware limits pilot scale and model choices; record out-of-memory
   and compatibility failures as infrastructure outcomes.
7. Entity and attribute labels in synthetic data may overstate recoverability
   or produce artifacts; use controlled fictional records and state limits.

## Gate 0 work remaining

- Inspect full primary texts and appendices, especially language lists in the
  2024 multilingual and cross-script papers.
- Search and verify relevant 2026 research through the Gate 0 cutoff.
- Verify datasets, models, revisions, licenses, and Bangla/ROM/MIX coverage.
- Select attacker capabilities, primary endpoints, sample construction,
  comparisons, and a feasible pilot.
- Review the resulting protocol for feasibility before Phase 5.
