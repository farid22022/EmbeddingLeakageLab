# Methodology and threat-model notes

**Status:** Provisional design for Gate 0; no attack, defense, or experiment has
been implemented or run.

## Comparison unit

Use a shared fictional semantic record as the unit of pairing. BN, ROM, EN, and
MIX are renderings of that record, not interchangeable observations. Track
translation, transliteration, code-switch edits, reviewer judgments, token
labels, and source-to-derived lineage. Preserve original strings alongside
Unicode-normalized copies. Split by semantic template before creating any
rendering so paraphrases and translations cannot cross train, validation, and
test splits.

## Text and language processing

Assign primary condition from the construction protocol and human review. MIX
requires token-level tags; whole-sentence language identification is not enough.
Keep Bengali script, Latin-script Bangla, English, and other/unknown spans
distinct. Store back-transliteration in a separate field and never replace raw
Romanized text. Count whitespace lexical tokens and model subword tokens
separately; document NFC handling, punctuation, Unicode grapheme behavior,
Bangla clitics, sentence truncation, and model-specific tokenizer version.
Mark excluded or truncated samples without deleting their provenance.

## Access and attack separation

For each future method, declare victim query permission and query count,
knowledge of model ID/architecture, access to weights/gradients, leaked
embedding-text pairs, auxiliary data size and distribution, attack-model
pretraining corpus, and attacker objective. “No victim queries” does not mean
“no auxiliary data.” Exact reconstruction, semantic recovery, retrieval,
membership inference, entity recovery, and attribute inference are distinct
tasks and cannot share one headline metric. Initially use one known-model,
black-box, query-access, synthetic-only scenario; any transfer/no-query setting
is a separately preregistered comparison.

## Outcomes and validity

Exact text uses raw and NFC-only match; character/token edit measures are
reported with script-aware units. Semantic equivalence is judged with a blinded
rubric and, secondarily, an independently selected multilingual evaluator.
Entity extraction is scored against fictional typed slots with exact and
normalized matching. Attribute inference uses held-out labels, macro-F1,
balanced accuracy, and label-prior baselines. Downstream utility requires a
separate held-out use task and is not a proxy for privacy. Do not use a victim
embedding model as the only semantic evaluator of its own inversion output.

## Statistical and reproducibility rules

Pair renderings at the template level. Use paired bootstrap intervals clustered
by template; select paired permutation or McNemar according to outcome type.
Register primary contrasts, effect sizes, sample size rationale, and Holm
correction family before confirmatory analysis. The small first pilot is
descriptive and for feasibility/variance estimates only. Record missing,
failed, and excluded cases. Freeze seed, data checksum, model/tokenizer IDs,
pooling, normalization, software, hardware, access budgets, runtime, and memory
in immutable run metadata. Keep any sensitive outputs local and untracked.

## Evidence limits

Existing literature establishes word-level and sentence-level leakage,
multilingual inversion, no-query transfer, few-shot alignment, and several
defenses. A 2024 20-language evaluation includes five Indo-Aryan conditions but
not Bengali in its enumerated test languages. This only confirms a specific
coverage gap in that paper; it does not establish global novelty. See the
literature verification log for search scope and unresolved sources.
