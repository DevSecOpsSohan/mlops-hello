# Lesson 09 — MLflow: Experiment Tracking 📊

Phase 2 — Core MLOps Tooling. Track every training run (params, metrics, model) so
results never vanish and the best run is reproducible. Serves the **Reproducibility**
+ **Governance** pillars.

## Files
- `train_mlflow.py` — trains the Iris model and logs the run to MLflow
- `mlflow.db` — SQLite DB holding run metadata (params/metrics) — git-ignored
- `mlruns/` — model artifacts — git-ignored (generated data)

## How to run
```bash
python train_mlflow.py                              # trains + logs one run
mlflow ui --backend-store-uri sqlite:///mlflow.db   # open http://127.0.0.1:5000
```

> ⚠️ **MLflow 3.x storage note:** this version stores run metadata in a **SQLite database
> (`mlflow.db`)**, NOT the old `meta.yaml` files inside `mlruns/`. So the UI must be pointed
> at that DB with `--backend-store-uri sqlite:///mlflow.db`, or it'll look empty. The script
> sets `mlflow.set_tracking_uri("sqlite:///mlflow.db")` so everything stays consistent.

---

## 📂 Where MLflow stores everything (MLflow 3.x)

MLflow splits your data into **two places**: a database for *metadata* and a folder for *files*.

### 1. `mlflow.db` (SQLite database) — the **metadata / structured data**
Everything you can put in a table lives here. Peek inside with any SQLite viewer. Key tables:
| Table | Holds |
|-------|-------|
| `experiments` | your experiments (e.g. `iris-classifier`) |
| `runs` | each run (id, start time, status) |
| `params` | logged parameters (`max_iter=200`) |
| `metrics` / `latest_metrics` | logged metrics (`accuracy=1.0`) |
| `tags` | run/experiment tags |
| `registered_models` / `model_versions` | the **Model Registry** (versions, stages) |
| *(new in 3.x)* `traces`, `spans`, `assessments`, `evaluation_datasets`, `scorers`, `guardrails` | GenAI/LLM tracing & evaluation features |

> 👉 So your **params, metrics, run records, and the model registry** are all in `mlflow.db` —
> that's the "other info you didn't see" in the folder.

### 2. `mlruns/` folder — the **artifacts (actual files)**
Things too big/binary for a database — the saved models and how to reproduce them.
Structure: `mlruns/<experiment-id>/models/m-<hash>/artifacts/`

| File | What it is |
|------|-----------|
| `MLmodel` | the model's descriptor — its **"flavors"**, input/output signature, load info |
| `model.skops` | the actual serialized model (`.skops` = newer *secure* sklearn format, safer than pickle) |
| `requirements.txt` | pip deps to reproduce the model's environment |
| `conda.yaml` | conda environment spec (same purpose, conda flavor) |
| `python_env.yaml` | the exact Python version/env used |

> 👉 `mlruns/` is created the moment you call `log_model(...)`. It exists to store the **model
> file + everything needed to reload and reproduce it** on another machine. This is MLflow's
> **Models** component (Reproducibility pillar) made physical.

### One-line mental model
> **`mlflow.db` = the searchable index (params, metrics, runs, registry).**
> **`mlruns/` = the file cabinet (the actual model files + their environment).**
> The UI reads the DB for the tables and the folder for the artifacts, and shows them together.

---

## 🎯 `set_tracking_uri()` and `get_tracking_uri()` — control WHERE data lives

### `mlflow.set_tracking_uri(uri)` — **tells** MLflow where to store/read tracking data (write)
```python
mlflow.set_tracking_uri("sqlite:///mlflow.db")
```
**Importance:** this one line decides where ALL your params, metrics, and models go. It's what
turns MLflow from a personal laptop tool into a **team platform**.

**The URI can be LOCAL or REMOTE:**
| URI form | Type | Where data goes |
|----------|------|-----------------|
| `sqlite:///mlflow.db` | local DB | a SQLite file next to your code (default name) |
| `sqlite:///mytracks.db` | local DB (custom name) | a SQLite file you named |
| `http://127.0.0.1:5000` | **remote (local server)** | a running MLflow server on your machine |
| `http://mlflow.mycompany.com:5000` | **remote (team server)** 🏢 | a shared central server — everyone logs here |
| `https://<databricks-workspace>` | **remote (managed cloud)** | Databricks / cloud-hosted MLflow |

> ⚠️ **File store is DEPRECATED in MLflow 3.x.** A bare folder path like `./mlruns` or
> `./mytracks` (the old file store with `meta.yaml` files) now raises an error telling you to
> *"migrate to a database backend (e.g., sqlite:///mlflow.db)"*. This is exactly why 3.x uses a
> SQLite DB and has no `meta.yaml`. **For a custom name, use `sqlite:///yourname.db`, NOT a folder.**

---

## 🗂️ `create_experiment()` and `set_experiment()` — organize runs into groups

An **experiment** is a **named group of related runs** (e.g. all your Iris runs together). It
keeps different projects separate and lets you compare only the runs that belong together.
Without experiments, every run would pile into one messy default bucket.

> ### 🧭 WHEN TO USE WHICH (the one thing to remember)
> - **`create_experiment(name)`** → for a **brand-new** experiment you're about to run.
>   **Errors if the name already exists.** It's the *only* place to set a custom artifact
>   location + tags.
> - **`set_experiment(name)`** → for an **existing** experiment (pass its name to keep logging
>   to it). **If no experiment with that name exists, it creates one** automatically, then
>   activates it. This is the everyday function.

### `mlflow.set_experiment(name)` — activate an experiment (create if missing)
```python
mlflow.set_experiment("iris-classifier")
```
- **Parameter:** `experiment_name` (or `experiment_id`).
- **What it does:** makes this experiment the **active** one — every run after this line is
  filed under it. If the experiment doesn't exist yet, it **creates it automatically**.
- **Use / importance:** the everyday function. You'll almost always use this. It's "get-or-create
  + activate" in one call, so it's safe to call on every run.

### `mlflow.create_experiment(name, artifact_location, tags)` — explicitly create a NEW experiment
```python
exp_id = mlflow.create_experiment(
    name="iris-classifier",
    artifact_location="s3://my-bucket/iris",   # optional: where artifacts go
    tags={"project": "iris", "team": "mlops"}, # optional: labels/metadata
)
```
- **Parameters:**
  - `name` (required) — the experiment name.
  - `artifact_location` (optional) — a custom place to store this experiment's artifacts (e.g. an S3 bucket). Great for cloud/team setups.
  - `tags` (optional) — a dict of metadata (team, project, purpose) for filtering/organizing.
- **What it does:** creates a **brand-new** experiment and returns its **ID**. ⚠️ It **errors if
  the experiment already exists** (unlike `set_experiment`).
- **Use / importance:** use when you need **control** — a custom artifact location or tags at
  creation time. Because it errors on duplicates, guard it:
  ```python
  if mlflow.get_experiment_by_name(name) is None:
      mlflow.create_experiment(name, tags={...})
  mlflow.set_experiment(name)   # then activate it
  ```

### 🔑 Which do I use?
| Situation | Use |
|-----------|-----|
| Just group my runs (99% of the time) | `set_experiment(name)` |
| Need a custom artifact location or tags at creation | `create_experiment(...)` then `set_experiment(...)` |

> **Why experiments matter:** they're how you keep "Iris model runs" separate from "fraud model
> runs" and compare only what belongs together. On a team, tags + artifact locations set here
> feed organization and governance — an MLOps-engineer concern.

### 📋 Reading an experiment's details (the Experiment object)
`set_experiment()` **returns** the Experiment object (so do `get_experiment(id)` and
`get_experiment_by_name(name)`). You can read/print its attributes:
```python
experiment = mlflow.set_experiment("iris-experiment")
print(experiment.name)               # iris-experiment
print(experiment.experiment_id)      # 3
print(experiment.artifact_location)  # file:///.../iris_artifacts  <- the artifact URL
print(experiment.tags)               # {'project': 'iris', 'team': 'mlops-learning'}
print(experiment.lifecycle_stage)    # active
```

### 🗂️ Custom artifact location (a separate artifact URL per experiment)
By default, an experiment's artifacts go into `mlruns/`. But `create_experiment` lets you give
each experiment its **own** artifact home — a local folder, or a cloud bucket:
```python
from pathlib import Path
artifact_uri = Path("iris_artifacts").absolute().as_uri()   # -> file:///.../iris_artifacts
# or a cloud bucket:  "s3://my-bucket/iris"  /  "gs://my-bucket/iris"

mlflow.create_experiment(name="iris-experiment",
                         artifact_location=artifact_uri,
                         tags={"project": "iris"})
```
Now that experiment's models are stored under `iris_artifacts/` instead of `mlruns/`.
> ⚠️ **`artifact_location` is set ONCE at creation and can't be changed later.** That's why we
> used a fresh experiment name (`iris-experiment`) to see a *custom* location take effect — an
> experiment that already exists keeps its original location.
>
> 🏢 **Why this matters on a team:** you point each experiment's artifacts at shared cloud
> storage (S3/GCS/Azure) so models aren't trapped on one laptop. Designing that layout is an
> MLOps-engineer (governance) job.

> 🌉 **Remote is the real-team setup:** you run **one central MLflow server** (a remote URL), and
> every data scientist sets `mlflow.set_tracking_uri("http://mlflow-server:5000")`. Now all
> experiments land in one shared, comparable place instead of being trapped on individual laptops.
> Standing up and running that remote server is a core **MLOps-engineer (infra)** job — your DevOps strength.
> The remote server itself stores runs in a **backend store** (a real DB like PostgreSQL/MySQL) +
> an **artifact store** (S3, GCS, Azure Blob) for the model files.

### `mlflow.get_tracking_uri()` — **asks** MLflow where it's currently pointing (read)
```python
print(mlflow.get_tracking_uri())   # → sqlite:///mlflow.db
```
**Importance:** your #1 debugging tool. If runs aren't showing up where you expect, this tells
you where they *actually* went. (Rule: `set_` = write/tell, `get_` = read/ask.)

### ⚠️ IMPORTANT — if you DON'T set a custom path
If you never call `set_tracking_uri()`, MLflow uses a **default**: it auto-creates an **`mlruns/`
folder inside your current working directory** (wherever you run the script from). On a Windows
laptop that means it gets dumped somewhere on the **C: drive** next to your code — often not where
you want it, and easy to lose track of.

> ✅ **Best practice:** always set your own explicit tracking location so you control where data
> lands and it stays consistent:
> ```python
> mlflow.set_tracking_uri("sqlite:///mlflow.db")   # or a full custom path / remote server
> ```
> Then launch the UI pointing at the same place: `mlflow ui --backend-store-uri sqlite:///mlflow.db`.
> Don't rely on the default `mlruns/` — name it yourself.

---

## What is MLflow?
**MLflow is an open-source platform to manage the machine learning lifecycle.** It solves
the problem that training results normally print to the terminal and are lost — MLflow
records every run so you can compare experiments and reproduce the best model.

It has **4 major components:**

### 1. 📈 Tracking
Records and compares training runs so results don't vanish once the script finishes.
It logs **parameters** (settings you chose, e.g. `max_iter`), **metrics** (results you
measured, e.g. `accuracy`), the **code version**, and **artifacts** (files like the model).
A web **UI** lets you compare runs side by side.

### 2. 📦 Projects
Designed to **simplify packaging, reproducibility, and sharing of ML code.** It lets you
package code + dependencies into a reproducible format (described by an **`MLproject`**
file: environment, parameters, entry points) so experiments run the same across different
machines/environments.

### 3. 🤖 Models
Designed to **streamline deploying models to different environments.** It packages a trained
model into a **standard format** supported by many downstream tools in the pipeline. The model
is saved in multiple **"flavors"**, supporting libraries like **scikit-learn, TensorFlow,
PyTorch, Keras, Spark MLlib**, etc.

### 4. 🗂️ Registry
A **centralized, versioned repository** for managing models, their versions, and metadata.
It provides APIs + a UI to manage a model's **entire lifecycle** (e.g. promote a version to
*Staging* → *Production*), lets teammates **share** models, supports **search** by name/metadata,
and stores metadata (author, creation date, description) for each version.

> 🔑 Memory hook: **Tracking** = record runs · **Projects** = package code · **Models** =
> package the model · **Registry** = version + share + promote models.

---

## The MLflow API used here (only 4 calls)
```python
mlflow.set_experiment("iris-classifier")          # name the group of runs
with mlflow.start_run():                           # record ONE run
    mlflow.log_param("max_iter", 200)              # a PARAMETER (input setting)
    mlflow.log_metric("accuracy", acc)             # a METRIC (result number)
    mlflow.sklearn.log_model(model, name="model")  # an ARTIFACT (the model file)
```

## Key terms
| Term | Meaning | Example |
|------|---------|---------|
| Parameter | input setting you chose | `max_iter=200` |
| Metric | result number you measured | `accuracy=1.0` |
| Artifact | file the run produced | the trained model |
| Run | one execution of training | "run #3, 100% acc" |
| Experiment | a named group of runs | `iris-classifier` |

## 📝 Core logging functions (6) — `demo_logging.py`

These record data INTO a run. Singular = one at a time; plural = many via a dict
(except artifacts: singular = one file, plural = a folder).

| Function | Logs | Input | Returns |
|----------|------|-------|---------|
| `log_param(key, value)` | **one** param | 2 values | **the value** ⭐ |
| `log_params({...})` | **many** params | a dict | `None` |
| `log_metric(key, value, step=None)` | **one** metric | 2 values (+ optional step) | `None` |
| `log_metrics({...}, step=None)` | **many** metrics | a dict | `None` |
| `log_artifact(file_path)` | **one file** | a file path | `None` |
| `log_artifacts(dir_path)` | **all files in a folder** | a directory path | `None` |

**Important notes:**
- **Param vs Metric:** a **param** is an *input you chose* (`max_iter=200`, logged once); a
  **metric** is a *result you measured* (`accuracy=0.97`). Metrics accept a **`step`**, so you can
  log the same metric repeatedly (e.g. once per epoch) to form a **curve over time**:
  ```python
  for epoch in range(10):
      mlflow.log_metric("loss", loss, step=epoch)
  ```
- **Artifact vs Artifacts is different** from the others — it's **one file vs a whole folder**,
  not value vs dict. `log_artifact("plot.png")` uploads one file; `log_artifacts("reports/")`
  uploads every file in that directory.
- **Only `log_param` returns a value** (the value you logged). All the others return `None`.

### 📦 What is an "artifact" (and why store it)?
An **artifact = any FILE a run produces that you want to keep** — the trained model, plots
(confusion matrix, ROC curve), reports (`metrics.json`), data samples, config/env files.
> Metrics say *"how good was it?"* (a number). **Artifacts say *"show me the actual thing"*** (the model, the plot).

**Why store them:** reproducibility (recreate the exact output), debugging (open the real plots),
comparison (run #3 vs #7 side by side), sharing (teammates download from the UI),
governance/audit (prove what a model was), and deployment (the model artifact is what you ship).

**The two functions + optional `artifact_path` (a subfolder to organize inside the run):**
```python
mlflow.log_artifact("confusion_matrix.png", artifact_path="plots")  # ONE file -> <run>/artifacts/plots/
mlflow.log_artifacts("reports", artifact_path="reports")            # a FOLDER  -> <run>/artifacts/reports/
```

Runnable demos (split by group): **`logging-functions/`** — `demo_params.py`, `demo_metrics.py`,
`demo_artifacts.py` (run via `run_demos.py`, one at a time).

## 🎤 Interview note
> "MLflow is an open-source ML lifecycle platform with four components: Tracking (log params,
> metrics, artifacts per run), Projects (package code reproducibly via an MLproject file),
> Models (save models in standard 'flavors' for any framework), and the Model Registry
> (versioned central store to manage and promote models to staging/production). I use Tracking
> to compare runs and pick the best model, then register it for deployment."

## 🔁 Rebuild-from-memory test
- [ ] Name and explain the 4 MLflow components from memory (~2 weekends out).
