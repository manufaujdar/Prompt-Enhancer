# System architecture

Prompt Enhancer is currently a single-process FastAPI service with an in-memory
model pipeline.

## Startup

Process start -> import main.py -> load the microsoft/promptist Transformers
pipeline -> expose FastAPI routes.

If model loading fails, the process remains importable with the enhancer set to
None. /health reports model_loaded false and /enhance returns 503.

## Request flow

Client -> CORS middleware -> Pydantic PromptRequest validation -> empty-text
check -> Promptist pipeline -> PromptResponse.

The service does not persist prompts, maintain users, or call a database.
Logging currently includes a truncated prompt prefix, which requires a privacy
review before production use.

## Deployment boundary

render.yaml declares a Python web service with a Hugging Face cache path. The
current all-interface binding and wildcard CORS should be treated as demo
configuration. Production requires an explicit origin policy, request limits,
authentication or a local-only boundary, readiness semantics, and model
revision pinning.

## Extension points

Separate request schemas, model loading, enhancement service, health/readiness,
and observability into modules. A provider/model adapter should expose model
revision, runtime requirements, input/output limits, and failure behavior.

