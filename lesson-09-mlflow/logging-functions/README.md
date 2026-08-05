# MLflow Logging Functions — the 6 that record data into a run 📝

These functions put data INTO a run. Split into 3 files by group so you can study
one idea at a time (run them via `run_demos.py`, one uncommented at a time).

| File | Functions | Group |
|------|-----------|-------|
| `demo_params.py` | `log_param`, `log_params` | **Params** — inputs you chose |
| `demo_metrics.py` | `log_metric`, `log_metrics` | **Metrics** — results you measured |
| `demo_artifacts.py` | `log_artifact`, `log_artifacts` | **Artifacts** — files the run made |
| `demo_tags.py` | `set_tag`, `set_tags` | **Tags** — labels to organize/search runs |

## The 6 functions at a glance
| Function | Logs | Input | Returns |
|----------|------|-------|---------|
| `log_param(key, value)` | one param | 2 values | **the value** ⭐ |
| `log_params({...})` | many params | a dict | `None` |
| `log_metric(key, value, step=None)` | one metric | 2 values (+ step) | `None` |
| `log_metrics({...}, step=None)` | many metrics | a dict | `None` |
| `log_artifact(file_path, artifact_path=None)` | one **file** | a file path | `None` |
| `log_artifacts(dir_path, artifact_path=None)` | all files in a **folder** | a dir path | `None` |

## Important notes
- **Param vs Metric:** a **param** is an *input you chose* (`max_iter=200`, logged once); a
  **metric** is a *result you measured* (`accuracy=0.97`). Metrics accept a **`step`** so you can
  log the same metric over time (once per epoch) → a **curve** in the UI.
- **Singular vs plural:** singular = one at a time; plural = many via a **dict**
  (`log_params`, `log_metrics`).
- **Artifacts are different:** singular = one **file**, plural = a whole **folder** — not value vs dict.
- **Only `log_param` returns a value**; every other function returns `None`.

## 📦 What is an "artifact" (and why store it)?
An **artifact = any FILE a run produces that you want to keep** — the trained model, plots
(confusion matrix, ROC curve), reports (`metrics.json`), data samples, config/env files.
> Metrics say *"how good was it?"* (a number). **Artifacts say *"show me the actual thing"*** (the model, the plot).

**Why store them:** reproducibility (recreate the exact output), debugging (open the real plots),
comparison (run #3 vs #7), sharing (teammates download from the UI), governance/audit (prove what
a model was), deployment (the model artifact is what you ship).

**`artifact_path`** (optional) = a subfolder inside the run's artifact store to organize files:
```python
mlflow.log_artifact("confusion_matrix.png", artifact_path="plots")   # -> <run>/artifacts/plots/
mlflow.log_artifacts("reports", artifact_path="reports")             # -> <run>/artifacts/reports/
```

## 🏷️ Tags — `set_tag` / `set_tags`
A **tag** is a **label (key=value string)** you attach to a **run** to organize it and later
**search/filter** by it.

| Function | Sets | Input | Returns |
|----------|------|-------|---------|
| `set_tag(key, value)` | **one** tag | 2 strings | `None` |
| `set_tags({...})` | **many** tags | a dict | `None` |

**Limits:** key = string up to **250** chars · value = string up to **5000** chars.

**Tags are searchable** — filter runs by a tag (in the UI or via `search_runs`):
```python
mlflow.set_tag("stage", "production")                 # inside a run
mlflow.set_tags({"author": "sohan", "release": "v1"})

# later, find runs by tag — query syntax:  tags.<key> = '<value>'
mlflow.search_runs(filter_string="tags.author = 'sohan'")
```

> ⚠️ **Run tags vs experiment tags:** `set_tag`/`set_tags` tag the **current run** (call them
> inside an active run). To tag the **experiment itself**, use `create_experiment(tags={...})`
> or `mlflow.set_experiment_tag(key, value)`.
>
> 💡 **Tag vs Param:** a param is an *input to the model* (`max_iter=200`); a tag is *metadata
> about the run* (`stage=production`, `author=sohan`) used to organize and search.

## Run it
```bash
python run_demos.py                                  # keep one demo uncommented
mlflow ui --backend-store-uri sqlite:///mytracks.db  # then view at http://127.0.0.1:5000
```
