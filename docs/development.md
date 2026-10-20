# Local development and repository map

This is a small model-backed API demo. Start with the [technical baseline](technical-overview.md)
for known validation and hosting gaps, and the [API examples](../README.md#api-endpoints)
for request/response shapes.

## Set up an isolated environment

From the repository root:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Installing the current unpinned requirements can resolve different versions over
time. Importing the application attempts to load `microsoft/promptist`; a first
run can download model files and requires suitable memory/network access. Use
synthetic prompts for local work. The current code logs prompt prefixes.

`GET /` reports that the API process responds. `GET /health` always returns the
status text `healthy`, while `model_loaded` separately reports model availability.
Inspect that flag before trying `/enhance`; the status string alone is not a
model-readiness guarantee. The example generated text is illustrative.

## File ownership

| Location | Purpose |
| --- | --- |
| [main.py](../main.py) | App, request/response models, model initialization and all routes |
| [requirements.txt](../requirements.txt) | Current Python dependencies |
| [render.yaml](../render.yaml) | Existing hosted-service declaration |
| [README.md](../README.md) | Human entry and API examples |
| [docs/](DOCUMENTATION_INDEX.md) | Architecture, development and validation baseline |

Keep API instructions next to these existing documents. A package split should
follow a concrete implementation need; moving this single-file app adds no
current navigation benefit. Keep virtual environments, model caches and local
request data out of commits.

## Validate a documentation change

Check relative links and `git diff --check` without importing `main.py`. The
repository currently has no test suite or Actions workflow; these checks do not
establish model quality, endpoint behavior or deployment readiness. The proposed
fake-pipeline test cases and hosting gaps remain in the [technical overview](technical-overview.md#validation-gaps).

For application work, record the exact Python/dependency/model revision and
actual commands/results before making readiness claims. Choose license and
model redistribution terms explicitly rather than treating public visibility
as a license.
