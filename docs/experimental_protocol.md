# Experimental protocol (provisional; Gate 0 review)

**Status:** Feasibility-reviewed protocol plan, not an executable attack
implementation. Phase 0 does not authorize downloading large checkpoints or
running inversion. RQs and the pilot below remain subject to human approval.

## 1. Pilot objective and scope

The first future pilot will check dataset alignment, label quality, embedding
generation, memory use, and metric implementation on fictional synthetic text.
It will not estimate population-level privacy risk or compare defenses.

- Construct 64 fictional semantic records from 16 templates, with four
  non-identifying fictional slots (name, city, age band, preference). A bilingual
  Bangla-English annotator creates BN, ROM, EN, and MIX versions for each
  record. Store raw variants, transliteration/translation provenance, labels,
  and reviewed semantic-equivalence judgments separately.
- Assign the 16 template groups before generating variants: 10 train, 2
  validation, 4 test. All four language variants and all paraphrases of a
  template stay in one split. Use training data only for the selected attack's
  declared auxiliary pairs; validation only for model selection; hold out test
  pairs and labels.
- Use one approved, already-cached, CPU-compatible sentence encoder initially.
  The final model ID/revision, tokenizer revision, architecture, pooling,
  prompt, normalization, dimension, and license must be recorded before
  execution. A Bangla-capable victim is required; if no suitable cached model is
  available, the pilot is blocked pending a human model choice. Do not infer
  Bangla capability from a model card's generic “multilingual” label.
- Initial sequence bounds: 5–50 Unicode whitespace-delimited lexical tokens.
  Record whitespace counts and model subword counts separately; report length
  bands 5–10, 11–25, and 26–50 only if each has adequate examples. Define a
  Unicode-aware lexical-token rule and validate it manually for Bangla
  punctuation and clitics before the split. Do not force balanced length bins
  by dropping examples after seeing results.

## 2. Conditions and text handling

- **BN:** Bengali language primarily in Bengali script.
- **ROM:** Bangla written in Latin script. Preserve the original spelling;
  store any back-transliteration as a separate derived field with provenance.
- **EN:** English rendering of the same fictional proposition.
- **MIX:** Bangla-English code-switching with token-level language/script tags.
  Define at least one Bangla and one English token in the sentence; do not rely
  on whole-sentence language detection.
- Record `sample_id`, `template_id`, split, raw text, condition, script, token
  spans, token-level language label, transformation type, annotator review,
  fictional entity/attribute labels, source/derived text links, and a content
  checksum. Keep normalization outputs separate from raw text.
- A translation, transliteration, or mixed rewrite is not presumed equivalent.
  Two bilingual reviewers independently check whether all labeled facts are
  preserved; resolve disagreements before embedding. Record agreement and
  unresolved examples, and exclude unresolved pairs from the aligned primary
  analysis while retaining them in the manifest with exclusion reasons.
- Natural corpora (e.g., BanglaTLit or BanglaMix) are not the initial leakage
  target. If proposed later, review license/terms, provenance, privacy, source
  duplicates, identifiers, and annotation noise first. Do not treat a
  back-transliteration benchmark or code-mix classification corpus as an
  embedding-inversion benchmark.

## 3. Threat-model declaration

Access axes are declared independently for every attack; “black box” alone is
not a complete threat model.

| Axis | Pilot choice or required record |
|---|---|
| Target asset | Leaked fixed-length sentence vectors and fictional test texts as ground truth for evaluation; no victim labels leaked unless explicitly stated. |
| Victim query access | Primary future pilot: allowed only for encoding attacker-provided auxiliary/training text and, for a query-based corrector, attacker hypotheses. Record number and purpose of calls. A no-query transfer scenario is a separate experiment. |
| Victim identity/architecture | Declare known versus unknown before attack. Primary pilot: known model ID and representation recipe. Unknown identity is a separate condition. |
| Victim weights/gradients | Not available (black-box). White-box access is excluded from this project's initial comparison. |
| Paired auxiliary data | Report exact size, source, language composition, overlap controls, and whether pairs contain victim vectors. Pilot uses 0, 16, and 64 synthetic train pairs as explicitly labeled data budgets; these are separate conditions, not pooled. |
| Limited auxiliary data | Means at most 64 paired synthetic samples in this pilot. This is a project budget, not a claim that 64 is universally “few-shot”; later sensitivity budgets need preregistration. |
| Attacker text corpus | None beyond the explicitly listed synthetic training pairs for the pilot. Any pretrained attack generator has its own external pretraining and must be disclosed; no undisclosed corpus or API. |
| Attacker objective | Exact text, semantic proposition, entity slot, or attribute label are distinct endpoints. No claim of unique inverse text because pooled embeddings are non-injective. |
| Defender | No defense in the pilot. Later defense study must compare matched unprotected and protected embeddings under the same attack and access budget. |

Do not combine query-access Vec2Text-style evaluation, no-victim-query
transfer attacks, and white-box attacks into a single score.

## 4. Primary outcomes and reporting

Report separately by language condition, length band, and auxiliary-pair
budget:

1. Exact string match under NFC-only canonicalization; also raw exact match.
2. Character error rate and word/token error rate with metric tokenization
   documented. Bangla Unicode grapheme clusters are not interchangeable with
   bytes or whitespace words; publish the chosen unit and a sensitivity check.
3. Blinded human semantic-equivalence rate under a written rubric; automated
   semantic similarity is secondary and may not use only the victim encoder.
4. Entity exact-span and normalized-slot precision/recall/F1, plus per-record
   entity exposure rate.
5. Per-attribute macro-F1 and balanced accuracy, compared with majority and
   label-prior baselines.
6. For later defense work, utility on an independently held-out, approved task
   (initial candidate: paired semantic retrieval Recall@1/5/10) and the absolute
   change relative to unprotected vectors. Utility does not count as a privacy
   metric.

Report sample counts, exclusions, missing outputs, failed generations, and
confidence intervals alongside every metric. Preserve model outputs privately;
publish only fictional examples or aggregate results.

## 5. Statistical plan

- Treat template group as the independent sampling unit; transformed variants
  within a template are paired. Do not treat four renderings as four independent
  semantic examples.
- Before confirmatory work, choose one primary endpoint and contrasts. For
  pilot descriptive estimates, report paired bootstrap 95% intervals by
  template group (10,000 resamples, fixed and recorded seed). Use paired
  permutation for continuous paired differences; use McNemar only for paired
  binary outcomes. Report effect sizes and raw paired counts.
- If multiple confirmatory contrasts are approved, use Holm correction within
  the declared family. No significance wording for exploratory pilot results;
  no post-hoc selection of model, metric, language pair, or length band as the
  primary result.
- A pilot with 16 held-out templates is for feasibility and variance
  estimation only, not a powered hypothesis test. Set a larger sample size only
  from an explicit power/precision calculation and approved data plan.

## 6. Resource and reproducibility limits

- Hardware planning values supplied by the project owner: Intel i5-1135G7,
  12 GB RAM, NVIDIA MX450 with 2 GB VRAM, Intel Iris Xe. Current runtime
  verification reports CPU and no CUDA; the inventory itself has not been
  independently verified.
- CPU-first, one cached model, one process, batch size 4 (reduce to 1 if memory
  pressure), maximum sequence length 128 subword tokens, sequential language
  conditions, and no large checkpoint downloads. Set a 2 GB process-RAM
  warning threshold and a 5 GB hard stop for the pilot; record peak memory,
  encode/attack wall time, machine/software versions, and any throttling or
  failures. Model loading may exceed this budget; verify its footprint before
  starting and stop if it does.
- Every future run gets an immutable unique ID, frozen config, content checksum,
  model/tokenizer revision, seed, library versions, hardware, timestamps,
  runtime/memory, metrics, warnings, and status. Do not overwrite runs.
- This plan is not permission to implement an attack, defense, use sensitive
  real-world data, or start Phase 2. The Phase 0 and Phase 1 gates require human
  review.
