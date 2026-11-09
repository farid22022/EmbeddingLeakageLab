# Literature review index

**Review status:** Preliminary; Phase 0 remains open.
**Last checked:** 2026-11-09.
**Verification basis:** Publisher proceedings pages or arXiv records; see
`verification_log.md`.

## Starting set

| Work | Main contribution relevant here | Relevance and limitation |
|---|---|---|
| Morris et al. (2023), [Text Embeddings Reveal (Almost) As Much As Text](https://aclanthology.org/2023.emnlp-main.765/) | Iterative Vec2Text inversion; reports exact reconstruction in its studied setting and recovery of names from clinical notes. | Core attack baseline; reported performance is setting-specific, not a project expectation. |
| Li et al. (2023), [Sentence Embedding Leaks More Information than You Expect (GEIA)](https://aclanthology.org/2023.findings-acl.881/) | Trains/fine-tunes a decoder to generate sequences from sentence embeddings. | Relevant generative attack; training/data/model requirements must be evaluated for feasibility. |
| Chen et al. (2024), [Text Embedding Inversion Security for Multilingual Language Models](https://aclanthology.org/2024.acl-long.422/) | Defines multilingual and cross-lingual inversion; studies multilingual models and masking defense. | Establishes that multilingual inversion and defense comparisons are not novel by themselves. Language coverage must be checked in full text. |
| Huang et al. (2024), [Transferable Embedding Inversion Attack](https://aclanthology.org/2024.acl-long.230/) | Uses a surrogate/transfer attack without direct victim-model access. | Threat-model baseline; do not conflate with query-access attacks. |
| Zhuang et al. (2024), [Understanding and Mitigating the Threat of Vec2Text](https://arxiv.org/abs/2402.12784) | Studies pooling, bottleneck pretraining, noise, quantization, dimensions, and privacy/retrieval tradeoffs; proposes a ranking-preserving transform. | Direct defense precedent. The arXiv version and SIGIR-AP 2024 publication need full method extraction. |
| Chen et al. (2024), [Against All Odds](https://arxiv.org/abs/2408.11749) | Studies cross-lingual and cross-script inversion across 20 languages, 8+ families, and 12 scripts; reports Indo-Aryan and script-related risk. | Strongly narrows novelty. Exact language list and Bangla inclusion require full-text/supplement verification. |
| Chen et al. (2025), [ALGEN](https://aclanthology.org/2025.acl-long.1185/) | Few-shot cross-model alignment and generation; studies cross-domain/language transfer and defenses. | Current comparison point; prompts a low-resource/limited-auxiliary-data threat model review. |
| Kabir et al. (2024), [BanglaEmbed](https://arxiv.org/abs/2411.15270) | Introduces lightweight Bangla sentence embedding models using cross-lingual distillation. | Candidate victim models; not itself an inversion/privacy study. Verify release, license, revision, architecture, and suitability. |

## Provisional gap map

Prior research already covers embedding inversion, generative inversion,
multilingual and cross-script inversion, transferable attacks, and multilingual
defenses. The candidate contribution is a controlled, resource-aware study of
Bangla script, Romanized Bangla, and Bangla-English code-switching, with
language/script-specific leakage and utility metrics. Whether those exact
conditions and comparable models/data are absent from prior work is unresolved.
Do not present this as a confirmed gap until the primary-paper audit is complete.

## Research conducted 2023–2026

The verified starting set covers 2023–2025. A systematic search of 2026
proceedings/preprints and source coverage in the closest multilingual studies
remains outstanding. The date range in this table is not a claim of exhaustive
coverage.
