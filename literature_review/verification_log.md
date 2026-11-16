# Literature verification log

**Checked:** 2026-11-16. **Review type:** Structured primary-source search and
targeted full-text extraction; not a systematic review with exhaustive database
coverage or dual independent screening.

## Search protocol

- **Sources searched:** ACL Anthology official records and PDFs; arXiv records,
  HTML, and PDFs; ICLR 2026 official proceedings; Data in Brief/PMC article
  record; official BdNC project website; linked author repositories where
  identified.
- **Date window:** January 2020 through 2026-11-16. Includes foundational
  2020 work and relevant inversion, defense, model, and data resources.
- **Search strings used:** “information leakage embedding models inversion
  Song Raghunathan”; “embedding inversion text embeddings Vec2Text GEIA”;
  “multilingual embedding inversion cross-script Bengali Bangla”; “Bangla
  Romanized code-mixed embedding privacy inversion”; “Bangla sentence embedding
  model”; “Bangla transliteration corpus dataset”; “Bengali-English code-mixed
  dataset”; “few-shot embedding inversion ALGEN”; “SPARSE embedding inversion
  defense 2026”; and targeted title/identifier searches for each named work.
- **Inclusion:** primary papers/resources directly on embedding inversion,
  inference/defense, Bangla sentence encoders, Romanized Bangla, code-mixing,
  or closely related dataset construction.
- **Exclusion:** secondary summaries as factual support; generic privacy work
  without an embedding relationship; unrelated Bengali NLP tasks unless they
  provide a dataset relevant to condition construction. Dataset papers are
  clearly labeled as not privacy evaluations.
- **Screening and extraction:** verified citation metadata from official
  proceedings/preprint/publisher records; extracted language list, data,
  methods, metrics, and constraints from full text where available. Matrix cells
  state NOT REPORTED or pending where not inspected. This review is not
  exhaustive, and literature published or indexed after the cutoff is outside
  scope.

## Coverage finding: Bengali and related conditions

- Chen, Lent, and Bjerva (ACL 2024) evaluate English, French, German, and
  Spanish in the reviewed main tables. No Bangla, Romanized Bangla, or MIX
  condition identified.
- Chen et al., *Against All Odds* (arXiv v2, 2024-12-16), enumerate 20 test
  languages: Arabic, Urdu, Kazakh, Mongolian, Hindi, Gujarati, Punjabi,
  Chinese, Hebrew, Japanese, German, Turkish, Amharic, Sinhala, Korean,
  Finnish, Hungarian, Yiddish, Maltese, and Meadow Mari. Bengali is mentioned
  as related prior safety work, not included in that test list. No Romanized
  Bangla or code-switch condition identified. The paper reports 600K training
  examples for Hindi/Gujarati/Punjabi/Urdu, 1M for selected other training
  languages, 500 evaluation examples per language, four AMD MI250 GPUs, and
  approximately 40,000 GPU hours overall.
- ALGEN (ACL 2025) multilingual experiments use English, French, German, and
  Spanish; no Bangla/ROM/MIX condition identified. It reports MultiHPLT English
  decoder training, mMarco language data, up to 1K alignment pairs, and 200
  evaluation samples.
- BanglaTLit, BnSentMix, BanglaMix, and BdNC provide relevant script/mixed-data
  resources, but do not evaluate privacy leakage from sentence embeddings.
- Therefore: **Bangla inclusion is confirmed absent from these enumerated
  experiments, not from the entire literature.** The project must not claim
  “first” or global novelty from this bounded finding.

## Primary records checked

| Record | Primary source | Verified | Still open / caveat |
|---|---|---|---|
| Song & Raghunathan (2020), Information Leakage in Embedding Models | [ACM DOI](https://doi.org/10.1145/3372297.3417277), [arXiv](https://arxiv.org/abs/2004.00053) | CCS 2020 pages 377–390; word recovery, attribute inference, membership inference, defenses; abstract reports 50–70% word recovery F1 range | Exact tested model/corpus tables and scripts not fully extracted |
| Morris et al. (2023), Vec2Text | [ACL Anthology](https://aclanthology.org/2023.emnlp-main.765/) and local PDF | EMNLP citation; English Wikipedia/MS MARCO/NQ/BEIR and clinical name case; iterative query feedback; 32-token result is setting-specific | Full configuration/pooling and every split remain to extract |
| Li et al. (2023), GEIA | [ACL Anthology](https://aclanthology.org/2023.findings-acl.881/) and local PDF | ACL Findings citation; PersonaChat/QNLI sizes and splits; SBERT/SimCSE/ST5/MPNet; GPT-2 decoder; token metrics and entity recovery | Pooling, dimensions, exact auxiliary data training budget not extracted |
| Chen et al. (2024), multilingual inversion | [ACL Anthology record](https://aclanthology.org/2024.acl-long.422/) and [PDF](https://aclanthology.org/2024.acl-long.422.pdf) | ACL citation; main language list English/French/German/Spanish; GTR/multilingual-e5, T5-family attacker; masking defense | Fine-grain datasets, sizes, pooling and resource details remain incomplete |
| Huang et al. (2024), transferable inversion | [ACL Anthology](https://aclanthology.org/2024.acl-long.230/) and [PDF](https://aclanthology.org/2024.acl-long.230.pdf) | ACL citation, no victim queries/model knowledge, leaked pairs, GTR-T5 surrogate/adapter, GPT decoder; SBERT/ST5/OpenAI victim, clinical case | Exact sample budgets and splits remain incomplete |
| Zhuang et al. (2024), Vec2Text retrieval/mitigation | [DOI](https://doi.org/10.1145/3673791.3698414), [arXiv](https://arxiv.org/abs/2402.12784) | SIGIR-AP citation and mitigation scope | Full methods/datasets/model IDs need direct paper extraction |
| Chen et al. (2024), Against All Odds | [arXiv record](https://arxiv.org/abs/2408.11749), [full text](https://arxiv.org/html/2408.11749) | v2 date, 20 languages, CulturaX sizes, mE5/GTR/mT5 models, query-based corrector, metrics, GPU scale, limitations | Preprint, no Bengali target evaluation; supplementary detail may refine counts |
| Chen et al. (2025), ALGEN | [ACL Anthology](https://aclanthology.org/2025.acl-long.1185/) and [PDF](https://aclanthology.org/2025.acl-long.1185.pdf) | Citation, four language experiments, victim models, mean pooling/L2 normalization, MultiHPLT/mMarco, 150K decoder samples, up to 1K alignment and 200 eval | Exact language-specific corpus sizes and complete limitations need review |
| Kabir et al. (2024), BanglaEmbed | [arXiv](https://arxiv.org/abs/2411.15270) | Title/authors/date and abstract; authors state ACAI 2024 acceptance | Proceedings entry, checkpoints, license, tokenizer/pooling and datasets remain unverified |
| Fahim et al. (2024), BanglaTLit | [ACL Anthology](https://aclanthology.org/2024.findings-emnlp.859/) and [PDF](https://aclanthology.org/2024.findings-emnlp.859.pdf) | Findings EMNLP citation; 42.7K/245.7K sample resources, task and author repository | Split/licensing details must be checked before reuse |
| Alam et al. (2025), BnSentMix | [ACL Anthology](https://aclanthology.org/2025.loreslm-1.4/) | 20K samples, 4 sentiment labels, Facebook/YouTube/e-commerce provenance | Script distribution, splits, and terms need full-text review |
| Seputis et al. (2025), reproducibility | [arXiv](https://arxiv.org/abs/2507.07700), local PDF, DOI [10.1145/3705328.3748155](https://doi.org/10.1145/3705328.3748155) | RecSys reproducibility-track oral acceptance; abstract findings on length sensitivity/noise/quantization | Detailed datasets, encoders and metrics are not yet transcribed into matrix |
| Tsai et al. (2026), SPARSE | [ICLR proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/01025a4e79355bb37a10ba39605944b5-Abstract-Conference.html), [full text](https://arxiv.org/html/2602.07090), local PDF | ICLR 2026; GTR-base/Sentence-T5/SBERT; STS12/FIQA and MIMIC examples; Vec2Text/GEIA/MLC; concept mask/Mahalanobis method; limitations and RTX 3090 24GB resources | Full six-dataset names and language coverage need extraction; no Bangla result identified |
| Afridi et al. (2026), BanglaMix | [Data in Brief/PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13685450/), [DOI](https://doi.org/10.1016/j.dib.2026.113317) | 2026-10-07 publication, 12,576 comments, 120,866 labeled tokens, five token labels, 500-example reliability check | Social media reuse requires separate terms/privacy/ethics review; silver-label limitations |
| BdNC and Romanized Bangla corpus | [Official project site](https://corpus.bangla.gov.bd/) | Site states 3B+ raw words and at least 200K Romanized Bangla words | Maintainer, release versions, sampling, splits, license, access, and auditability not verified |

## Review files and limits

- `comparison_matrix.csv` is the paper/resource-level extraction table. It
  distinguishes unavailable facts from established evidence; some detailed
  fields remain pending rather than guessed.
- `index.md` gives the reviewed sources and the primary conclusion.
- `research_gap.md` records supported, rejected, and unresolved claims.
- `references.bib` lists cited primary records; verify bibliography formatting
  again before manuscript submission.
- The six existing downloadable core PDFs and checksums remain registered in
  `papers/README.md` and `papers/SHA256SUMS.txt`. No additional large artifact
  or data was downloaded for this review.
