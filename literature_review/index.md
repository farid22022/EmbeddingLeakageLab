# Literature review index

**Review status:** Structured primary-source review prepared; Gate 0 remains
open pending human review and completion of detailed extraction fields.
**Last checked:** 2026-11-16. **Coverage:** 2020–2026-11-16; not exhaustive.
See [verification_log.md](verification_log.md) for search method and caveats.

## Core inversion and defense research

| Work | Verified contribution | Coverage and relevance |
|---|---|---|
| Song & Raghunathan (2020), [Information Leakage in Embedding Models](https://doi.org/10.1145/3372297.3417277) | Word recovery, attribute inference, membership inference, and defenses from embeddings. | Foundational; distinguishes endpoints beyond sentence reconstruction. |
| Morris et al. (2023), [Text Embeddings Reveal (Almost) As Much As Text](https://aclanthology.org/2023.emnlp-main.765/) | Vec2Text iteratively generates, queries, and corrects candidate text; ACL abstract reports 92% exact recovery for 32-token inputs in its evaluated setting. | English settings and clinical name recovery; result is not a Bangla expectation. |
| Li et al. (2023), [GEIA](https://aclanthology.org/2023.findings-acl.881/) | Decoder trained to generate ordered text from frozen sentence embeddings; evaluates token and entity recovery. | PersonaChat/QNLI and English models; token F1 is not exact text match. |
| Chen et al. (2024), [Text Embedding Inversion Security for Multilingual Language Models](https://aclanthology.org/2024.acl-long.422/) | Black-box multilingual and cross-lingual inversion plus masking defense. | Main audited languages English, French, German, Spanish; no Bangla/ROM/MIX condition found. |
| Huang et al. (2024), [Transferable Embedding Inversion Attack](https://aclanthology.org/2024.acl-long.230/) | Surrogate transfer attack when the victim model cannot be queried or identified. | English benchmark and clinical MIMIC-III case; paired leaked data remains an access assumption. |
| Zhuang et al. (2024), [Understanding and Mitigating the Threat of Vec2Text](https://doi.org/10.1145/3673791.3698414) | Studies retrieval risks and mitigation/utility effects. | Dense retrieval precedent; detailed comparison fields remain in the matrix as NOT REPORTED pending extraction. |
| Chen et al. (2024), [Against All Odds](https://arxiv.org/abs/2408.11749) | Cross-script and cross-family inversion across 20 languages and 12 scripts, with language-confusion analysis. | Includes Hindi, Gujarati, Punjabi, Urdu, Sinhala, but not Bangla in its enumerated test languages; requires very substantial compute. |
| Chen et al. (2025), [ALGEN](https://aclanthology.org/2025.acl-long.1185/) | Cross-model alignment and generation with low alignment-data budgets. | English, French, German, Spanish experiments; up to 1,000 alignment pairs; no Bangla/ROM/MIX condition found. |
| Seputis et al. (2025), [Rethinking the Privacy of Text Embeddings](https://doi.org/10.1145/3705328.3748155) | Vec2Text reproducibility, length sensitivity, and noise/quantization analyses. | Useful replication and defense-control context; not Bangla-specific. |
| Tsai et al. (2026), [SPARSE](https://proceedings.iclr.cc/paper_files/paper/2026/hash/01025a4e79355bb37a10ba39605944b5-Abstract-Conference.html) | Concept-sensitive dimension masking and Mahalanobis noise for privacy-utility tradeoffs. | ICLR 2026; reported tasks include STS12/FIQA and a MIMIC case; does not guarantee against membership inference. |

## Bangla models and data resources

| Resource | What it provides | What it does not establish |
|---|---|---|
| [BanglaEmbed](https://arxiv.org/abs/2411.15270) (Kabir et al., 2024) | Two lightweight Bangla sentence embedding models; authors state ACAI 2024 acceptance. | No embedding inversion evaluation; artifact license and exact model details remain to verify. |
| [BanglaTLit](https://aclanthology.org/2024.findings-emnlp.859/) (Fahim et al., 2024) | 42.7K Romanized Bangla transliteration pairs and a 245.7K pretraining corpus. | Not a code-switch or embedding privacy evaluation. |
| [BnSentMix](https://aclanthology.org/2025.loreslm-1.4/) (Alam et al., 2025) | 20K Bengali-English code-mixed sentiment samples from several sources. | Not an inversion benchmark; terms and exact script/split details need review. |
| [BanglaMix](https://doi.org/10.1016/j.dib.2026.113317) (Afridi et al., 2026) | 12,576 social comments, raw/clean text, Bengali transliteration, token labels (BAN/ENG/ROM_BAN/OTHER/UNK). | Silver-standard social-media resource, not an embedding privacy evaluation; project reuse requires separate governance review. |
| [BdNC](https://corpus.bangla.gov.bd/) | Official project site reports 3B+ raw words and at least 200K Romanized Bangla words. | Release/version, license, sampling and splits not verified in this review. |

## Coverage and gap boundary

The reviewed multilingual inversion papers establish that multilingual and
Indo-Aryan risk have already been studied. The enumerated 2024 20-language set
does not include Bengali; ACL 2024's audited language set and ALGEN's tested
language set also omit Bangla. The 2025 BanglaTLit and 2026 BanglaMix resources
cover transliteration or code-mix tagging, not embedding inversion. The
structured search did not find a direct Bangla/ROM/MIX sentence-embedding
inversion evaluation, but this is a bounded negative finding, not proof of
global novelty. See [research_gap.md](research_gap.md).

## Local paper copies and bibliography

The six user-prioritized PDFs remain in [`papers/`](papers/README.md), with
source/license notes and SHA-256 checksums. Additional primary references and
verified metadata are in [`../references.bib`](../references.bib). The full
source-by-source verification table is in [verification_log.md](verification_log.md).
