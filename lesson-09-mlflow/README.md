# Lesson 09 — MLflow: Experiment Tracking 📊

Phase 2 — Core MLOps Tooling. Track every training run (params, metrics, model) so
results never vanish and the best run is reproducible. Serves the **Reproducibility**
+ **Governance** pillars.

## Files
- `train_mlflow.py` — trains the Iris model and logs the run to MLflow
- `mlruns/` — where MLflow stores runs (git-ignored — generated data)

## How to run
```bash
python train_mlflow.py     # trains + logs one run
mlflow ui                  # open http://127.0.0.1:5000 to explore runs
```

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

## 🎤 Interview note
> "MLflow is an open-source ML lifecycle platform with four components: Tracking (log params,
> metrics, artifacts per run), Projects (package code reproducibly via an MLproject file),
> Models (save models in standard 'flavors' for any framework), and the Model Registry
> (versioned central store to manage and promote models to staging/production). I use Tracking
> to compare runs and pick the best model, then register it for deployment."

## 🔁 Rebuild-from-memory test
- [ ] Name and explain the 4 MLflow components from memory (~2 weekends out).
