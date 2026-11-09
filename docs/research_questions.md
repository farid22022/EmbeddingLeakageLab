# Research questions and hypotheses

These questions are provisional and must pass Gate 0. Their wording does not
assert that a gap or effect has been established.

## Questions

- **RQ1:** How much textual information can be recovered from embeddings of
  Bangla and multilingual text under defined attacker access assumptions?
- **RQ2:** How does inversion performance differ among BN, ROM, EN, and MIX?
- **RQ3:** How do model architecture, sentence length, language, and script
  affect leakage?
- **RQ4:** Can an attacker infer sensitive entities or attributes when exact
  reconstruction fails?
- **RQ5:** How do selected protection methods affect leakage across conditions?
- **RQ6:** What privacy–utility tradeoffs arise under the same controlled
  evaluation protocol?

## Hypotheses

- **H1:** Inversion performance differs by language and script condition.
- **H2:** Sentence length and embedding architecture affect reconstruction.
- **H3:** Semantic or entity information may remain recoverable when exact text
  reconstruction fails.
- **H4:** A protection method's effectiveness varies across language conditions.
- **H5:** Protection changes downstream embedding utility, with tradeoffs that
  may differ by condition.

## Interpretation constraints

Treat all hypotheses as unconfirmed. Define exact reconstruction, semantic
similarity, entity recovery, attribute inference, utility, and threat model
separately. Translation and transliteration do not guarantee semantic
equivalence. Do not claim statistical significance without a valid test and
predeclared comparison.
