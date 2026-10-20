# Documentation index

Prompt Enhancer is a small FastAPI service that loads Microsoft's Promptist
model and transforms submitted text prompts. The repository is public, but no
license is declared; it also lacks tests and production hardening.

## Current source of truth

- [README](../README.md): endpoint examples and local setup.
- [Local development](development.md): isolated setup, file placement and validation limits.
- [main.py](../main.py): current executable behavior.
- [render.yaml](../render.yaml): hosted-service intent.
- [Architecture](architecture.md): runtime and data flow.
- [Technical overview](technical-overview.md): code, dependency, operations, and gap baseline.

## Required initial set

| Area | Status |
| --- | --- |
| Product description and API examples | Present, needs verification |
| Architecture and data flow | Added |
| Code and technology map | Added |
| Test strategy and reproducible validation | Missing; add tests before release claims |
| Security, CORS, logging, limits, and deployment boundary | Gap record added |
| License and model/weight provenance | Human follow-up |

## Similar projects

Use FastAPI application structure, Hugging Face Transformers pipeline
contracts, and the Promptist model card as references. Do not infer model
quality, licensing, or resource requirements from this README alone.

