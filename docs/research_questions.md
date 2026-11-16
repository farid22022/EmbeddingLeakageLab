# Research questions and hypotheses

**Status:** Provisional, evidence-informed questions for human review at Gate 0.
No attack or defense results are claimed. Comparisons will use controlled
synthetic data first; natural-corpus replications are out of the pilot scope.

## Research questions

- **RQ1 (text):** Under a declared black-box, query-access threat model, how do
  exact and semantic reconstruction outcomes compare across Bengali script
  (BN), Romanized Bangla (ROM), English (EN), and Bangla-English mixed text
  (MIX) when the underlying fictional proposition is held constant?
- **RQ2 (entities):** How often are predeclared fictional named entities
  recovered, exactly or by entity type, in each condition when exact sentence
  reconstruction fails?
- **RQ3 (attributes):** How accurately can an attacker infer the explicitly
  encoded fictional attributes from embeddings, and how does this differ from
  a label-prior baseline?
- **RQ4 (utility, later phase):** How does a selected protection method change
  a preregistered, language-appropriate embedding utility task alongside the
  same leakage outcomes? This question is deferred until a defense and a
  defensible utility benchmark are approved.

## Hypotheses

H1–H3 are exploratory directional comparisons only; no ordering among BN, ROM,
EN, and MIX is assumed. Test direction and minimum effect of interest must be
registered after a pilot confirms metric reliability. RQ4 has no hypothesis
until a concrete defense and utility task are selected.

## Outcome definitions

- **Exact reconstruction:** Unicode string exact match after only a documented
  metric-specific canonicalization (NFC and line-ending normalization). Report
  raw exact match too; do not remove punctuation, normalize spelling, or
  transliterate for the primary exact score.
- **Semantic reconstruction:** A candidate is semantically equivalent only
  under blinded human annotation with a written rubric. Automatic multilingual
  similarity (if later selected) is secondary and must not use the victim
  embedding as its sole judge.
- **Entity recovery:** Precision, recall, and F1 for fictional entity spans and
  typed entity slots, with exact-span and normalized entity-value results
  separate. Report the fraction of source examples with at least one correct
  sensitive entity as a secondary exposure measure.
- **Sensitive attribute inference:** Macro-F1 and balanced accuracy per
  predeclared fictional attribute, compared with majority-class and label-prior
  baselines. No real person's traits are included.
- **Downstream utility:** A separate task measure, such as paired semantic
  retrieval Recall@k, with task data, split, and model fixed before testing.
  Utility is not inferred from cosine similarity alone.

## Interpretation limits

All findings will be specific to the selected model, pooling and normalization,
dataset construction, auxiliary-data budget, and access scenario. The broad
multilingual inversion and privacy-defense areas are established; this project
will not claim priority based only on Bangla or low-resource status.
