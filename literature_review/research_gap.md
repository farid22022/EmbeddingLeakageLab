# Research gap assessment (bounded review; human review requested)

**Review cutoff:** 2026-11-16. **Status:** Evidence-informed but not exhaustive;
no novelty claim is authorized by this document.

## What is already established

- Song and Raghunathan (2020) evaluate word recovery, attribute inference,
  membership inference, and defenses from embeddings.
- GEIA (2023) generates ordered text from embeddings and evaluates token and
  entity recovery; Vec2Text (2023) adds iterative correction with victim queries
  and reports high exact reconstruction in its selected English settings.
- ACL 2024 work studies multilingual/cross-lingual inversion and masking over
  English, French, German, and Spanish. A distinct 2024 cross-script study
  evaluates 20 languages, including Hindi, Gujarati, Punjabi, Urdu, and Sinhala
  (Indo-Aryan family), but does not enumerate Bangla, Romanized Bangla, or
  code-switched Bangla as test conditions.
- Transferable inversion (2024) evaluates a no-victim-query setting with leaked
  text/vector pairs and a clinical case study. ALGEN (2025) uses cross-model
  alignment and generation, with English/French/German/Spanish experiments and
  alignment budgets from one to 1,000 pairs. Reproducibility work revisits
  Vec2Text; SPARSE (ICLR 2026) adds concept-aware privacy perturbation and
  utility evaluation.
- Bangla sentence embedding research exists (BanglaEmbed). Romanized Bangla
  transliteration resources include BanglaTLit (42.7K paired samples, plus a
  245.7K pretraining corpus). Code-mix resources include BnSentMix (20K
  sentiment samples) and BanglaMix (12,576 comments with token tags and
  transliteration). These are not embedding inversion privacy evaluations.

## Candidate contribution status

**Partly supported, not proven novel:** a matched, resource-aware study of BN,
ROM, EN, and MIX leakage from sentence embeddings, under disclosed model/query
and auxiliary-pair budgets, measuring exact text, semantic propositions,
fictional entities/attributes, and later privacy-utility effects.

The reviewed papers’ named-language tables establish non-inclusion in those
specific evaluations. The structured search logged below did not identify a
directly matching Bangla embedding-inversion evaluation through the cutoff.
However, absence from a bounded search cannot prove no such work exists. The
claim should remain “not found in the reviewed sources,” pending expert review
and backward/forward citation searching.

## Coverage map

| Question | Status in prior work | Project opportunity |
|---|---|---|
| Can sentence embeddings leak words/text? | Established across 2020–2025 methods. | Replicate a selected baseline before comparing scripts; no new general inversion claim. |
| Multilingual and cross-script risk? | Directly explored, including several Indo-Aryan languages and 20-language study. | Test Bengali-specific behavior without claiming the first Indo-Aryan study. |
| No-query transfer and few-shot access? | Transfer attack and ALGEN address distinct restricted-data scenarios. | Treat budgets and query access as explicit factors; compare only if implementation/resources permit. |
| Romanized Bangla embedding inversion? | No direct study found in the reviewed sources; datasets exist for transliteration. | Controlled test with paired fictional content; model script support and spelling variation are key confounds. |
| Bangla-English code-switch embedding inversion? | No direct study found in the reviewed sources; general code-mix datasets exist. | Token-level tags and aligned synthetic comparison; avoid natural social data until governance is reviewed. |
| Entity/attribute leakage in Bangla? | Entity/attribute attacks exist in other language/domain settings; no direct Bangla evaluation found in reviewed set. | Test fictional structured slots and compare with simple label-prior baselines. |
| Language-specific privacy-utility defense? | Several defenses exist; SPARSE tests concept-aware leakage/utility on its selected tasks. | Defer until a usable baseline and language-valid utility dataset are available. Do not invent a defense contribution. |

## Obstacles and risk controls

1. Translation, transliteration, and code-switching can alter semantics and
   expose different clues. Use paired fictional records, independent bilingual
   review, provenance, and template-level splits.
2. Romanization is variable; exact string metrics may penalize equivalent
   spellings. Keep raw exact match primary and add a separately defined
   transliteration-aware analysis only as secondary.
3. Mixed text needs token-level language/script tags; sentence-level language
   detection is inadequate.
4. Language support, tokenizer coverage, pooling, prompts, normalization, model
   size, and license may invalidate a candidate encoder. Verify model artifacts
   before selection.
5. A 16-template test pilot is not powered for confirmatory significance. Use
   it for implementation feasibility and variance estimates only.
6. Published attacks often require large auxiliary corpora, pretrained
   decoders, substantial compute, or API access. The 12GB/2GB-VRAM planning
   hardware makes CPU-first small data suitable for a feasibility pilot, not a
   reproduction of 40,000-GPU-hour multilingual work.
7. Natural social-media data can include personal information despite public
   availability. Prefer synthetic data; review terms, provenance, and ethics
   before any natural-corpus use.

## Realistic contribution claims if supported by later evidence

- A reproducible paired synthetic benchmark protocol for four Bangla-related
  language/script conditions.
- A bounded measurement of reconstruction, fictional slot/entity recovery, and
  sensitivity to declared auxiliary data and query access for one or a small
  number of feasible models.
- A documented failure/compatibility analysis describing where evaluation is
  not possible with available language support or resources.
- A later matched privacy-utility comparison using an existing defense, only
  after language-appropriate utility data and defense feasibility are approved.

These are candidate contributions, not completed outcomes. The next research
task is expert review of the bounded search, then model/utility selection before
any Phase 2 or attack implementation begins.
