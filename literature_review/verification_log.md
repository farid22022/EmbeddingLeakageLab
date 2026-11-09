# Literature verification log

**Checked:** 2026-11-09. This is an initial verification pass, not an exhaustive
systematic review.

| Record | Primary source checked | Verified fields | Still to verify |
|---|---|---|---|
| Morris et al., 2023 | [ACL Anthology](https://aclanthology.org/2023.emnlp-main.765/) and [arXiv:2310.06816](https://arxiv.org/abs/2310.06816) | Title, authors, EMNLP 2023, DOI, abstract, reported setting | Complete method/dataset/model/metric details for matrix |
| Li et al., 2023 | [ACL Anthology](https://aclanthology.org/2023.findings-acl.881/) | Title, authors, Findings of ACL 2023, pages, DOI, method summary | Exact models, datasets, and full metric set |
| Chen et al., 2024 multilingual | [ACL Anthology](https://aclanthology.org/2024.acl-long.422/) | Title, authors, ACL 2024, pages, DOI, stated problem and defense | Exact languages/scripts, models, threat protocol, data, metrics |
| Huang et al., 2024 transfer | [ACL Anthology](https://aclanthology.org/2024.acl-long.230/) | Title, authors, ACL 2024, pages, DOI, no-victim-query premise | Exact data budget, languages, models, metrics |
| Zhuang et al., 2024 defense | [arXiv:2402.12784](https://arxiv.org/abs/2402.12784) and [University of Queensland publication record](https://about.uq.edu.au/experts-publication/28587/4751) | Title, authors, SIGIR-AP 2024 venue, DOI, defense scope | Dataset, exact model IDs, metric values, full method details |
| Chen et al., 2024 cross-script | [arXiv:2408.11749](https://arxiv.org/abs/2408.11749) | Title, authors, version history, abstract, 20 languages/12 scripts scope | Full language table and whether Bangla is included |
| Chen et al., 2025 ALGEN | [ACL Anthology](https://aclanthology.org/2025.acl-long.1185/) | Title, authors, ACL 2025, pages, DOI, abstract, stated data budget | Exact language list, model/dataset protocol, metrics, limitations |
| Kabir et al., 2024 BanglaEmbed | [arXiv:2411.15270](https://arxiv.org/abs/2411.15270) | Title, authors, date, abstract, author-stated ACAI 2024 acceptance | Proceedings metadata, model IDs, license, revisions, tokenizer/pooling |

The reference architecture [IntentGate](https://github.com/Atik203/IntentGate)
was inspected. Its visible repository combines a detailed README, source-of-
truth blueprint, phase roadmap, docs hub, literature review, experiment records,
tests, harness, configs, and CI. This project adopts those organization and
traceability practices, not its application code or domain logic.
