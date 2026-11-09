# Initial architecture

```text
YAML/config + roadmap ──> small CLI ──> human-readable status
                                      └─> environment report

Future, gated phases: data/provenance → embeddings → attacks/defenses →
evaluation → immutable experiment manifests → reports
```

The foundation uses a `src` package and console entry point. Runtime dependency
is limited to YAML parsing. Experiment and model components will be added only
when their roadmap phase is active and their contracts can be tested.
