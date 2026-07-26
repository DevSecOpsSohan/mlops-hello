# Lesson 08 — Testing with pytest 🧪

Phase 1 — SWE Foundations (final core skill). Automated tests that check the model
API and helper code still work on every change. Foundation for CI/CD (Phase 3).

## Files
- `calculator_funcs.py` — pure functions (from Project 3), no `input()` so they're testable
- `main.py` + `model.joblib` — the FastAPI app under test
- `test_calculator.py` — 5 unit tests for the pure functions
- `test_api.py` — 3 tests for the API via FastAPI TestClient

## How to run
```bash
pytest -v          # 8 passed
```

## What the tests cover
- **Pure functions:** add / subtract / multiply / divide + divide-by-zero message
- **API home:** GET `/` returns 200
- **API predict:** POST `/predict` with setosa features → 200 and `species == "setosa"`
  (this catches a broken/wrong model!)
- **API validation:** POST bad input → 422 (proves Pydantic guards the endpoint)

## Key concepts
- A test = call code with a known input, then `assert` the expected output.
- pytest auto-discovers `test_*` functions in `test_*.py` files.
- `assert` fails loudly and shows a diff (expected vs actual) — read it, it tells you the fix.
- `TestClient(app)` calls the API in-memory — no server needed, fast, CI-friendly.

## What I learned / bugs I hit
- Two tests failed first (`"0"` instead of the error string; `"setso"` typo). pytest's
  diff showed the exact correct value each time — reading the failure output IS the workflow.
- Warnings (httpx/numpy deprecations) are NOT failures — tests still pass.

## Why this matters for MLOps
In Phase 3 these tests run automatically on every `git push` (CI). If a code change breaks
`/predict` or the model output, the pipeline fails before it ever reaches production.

## 🔁 Rebuild-from-memory test
- [ ] Write a fresh `test_` function for one function without looking (~2 weekends out).
