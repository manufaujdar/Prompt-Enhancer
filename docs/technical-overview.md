# Technical overview

Status: public demo baseline; not production-ready.

## Runtime

- Python web service with FastAPI and Uvicorn.
- Pydantic request/response models are defined in main.py.
- Transformers loads microsoft/promptist; PyTorch supplies the runtime.
- requirements.txt is currently unpinned and there is no lockfile.
- render.yaml declares a hosted Python service.

## Code and API

main.py owns application construction, wildcard CORS, logging, model loading,
health routes, request/response models, enhancement, and the local entrypoint.
The documented endpoints are GET /, GET /health, and POST /enhance. The
response contains improved_prompt and original_prompt.

## Operations

Local development uses pip install -r requirements.txt and either python
main.py or Uvicorn reload. Model loading occurs at import time, so startup
latency and memory usage are part of the service behavior. Add readiness,
bounded input/output, concurrency controls, timeouts, and a model revision
before a hosted deployment.

## Validation gaps

There are no repository tests or CI checks. The minimum next test set covers
empty/whitespace input, malformed JSON, model-not-loaded behavior, successful
fake-pipeline behavior, model exceptions, response shape, CORS policy, and
startup/readiness behavior. CI should use a fake pipeline rather than download
weights.

## Security and provenance gaps

Wildcard CORS with credentials, all-interface binding, prompt-prefix logging,
unbounded input, unpinned dependencies, absent authentication, and missing
license/model provenance require human decisions. Review Promptist's model card,
weights, tokenizer, terms, and supply chain before redistribution or clinical
claims.

