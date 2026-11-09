# Methodology notes

## Comparability

Language-condition comparisons require documented source provenance, shared
sample identities where possible, fixed splits, and an explicit account of
translation/transliteration changes. Code-switched text needs a repeatable
definition. Token counts must specify tokenizer and handling of mixed scripts.

## Attack separation

Exact reconstruction, semantic similarity, retrieval, membership inference,
entity recovery, and attribute inference answer different questions. Report
them separately. Record victim-model query access and auxiliary-data assumptions
for each attack.

## Evaluation and statistics

Select metrics that match each outcome; preserve both raw and normalized text
for text metrics. Predeclare paired comparisons, confidence intervals, and
multiple-testing treatment before confirmatory experiments. No scores in this
repository are experimental results yet.
