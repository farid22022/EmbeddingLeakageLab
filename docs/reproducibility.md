# Reproducibility contract

Every future run must record a unique ID, dataset version and checksum, model
and tokenizer IDs/revisions, attack revision, immutable configuration/hash,
seed, environment, hardware, timestamps, metrics, runtime, memory, warnings,
errors, and status transitions. Never replace a completed run. Mark a run
validated or frozen only after separate checks. Keep raw/private data,
checkpoints, caches, credentials, and sensitive generated text out of Git.
