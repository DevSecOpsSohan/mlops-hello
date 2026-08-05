# MLflow Run Functions — start / end / active / last_active 🏃

These 4 functions control the **lifecycle of a single run** (one execution you track).
Each has its own demo file here so you can study one idea at a time. A run is where your
`log_param` / `log_metric` / `log_model` calls actually get recorded.

| File | Function | In one line |
|------|----------|-------------|
| `demo_start_run.py` | `mlflow.start_run()` | START a run (new, or resume an old one) |
| `demo_end_run.py` | `mlflow.end_run()` | END the active run manually (no `with`) |
| `demo_active_run.py` | `mlflow.active_run()` | get the run running RIGHT NOW (or `None`) |
| `demo_last_active_run.py` | `mlflow.last_active_run()` | get the LAST run, even AFTER it ended |

Run them via `run_demos.py` (uncomment one at a time).

---

## 1. `mlflow.start_run(...)` — begin a run

```python
mlflow.start_run(
    run_id=None,          # resume an EXISTING run by its id
    experiment_id=None,   # which experiment the NEW run goes under
    run_name=None,        # a friendly name for a NEW run
    nested=False,         # allow a run INSIDE another run
    tags=None,            # tags for the run (new or resumed)
    description=None,     # a text description for a NEW run
)
```

### Arguments — what each does, and when you CAN'T use it
| Argument | Meaning | Important rule |
|----------|---------|----------------|
| `run_id` | Resume/continue an **existing** run (by its id) | If you pass this, MLflow **reopens that run**. You then **cannot** use `run_name` or `experiment_id` — an existing run already has both. |
| `experiment_id` | Which experiment the **new** run belongs to | Only used **if `run_id` is NOT set**. If omitted, the active experiment is used (see precedence below). |
| `run_name` | A friendly name for a **new** run | Only for a **new** run (no `run_id`). If you don't give one, MLflow auto-generates a **unique random name** (e.g. "peaceful-crab-123"). |
| `nested` | Allow this run to sit **inside** another active run | Set `True` for a **nested run** (a run within a run — used for grouping sub-runs, e.g. per fold or per trial). Default `False`. |
| `tags` | key/value labels on the run | Works for **both** a new run and a resumed run (to add/update tags). |
| `description` | free-text notes for the run | For a **new** run (stored as the `mlflow.note.content` tag). |

### 🥇 Order of precedence — which EXPERIMENT does the run go to?
When you start a run, MLflow decides its experiment in this order (first match wins):
1. `experiment_id` passed to `start_run(...)`
2. the experiment set by **`mlflow.set_experiment(...)`**
3. the **`MLFLOW_EXPERIMENT_NAME`** environment variable
4. the **`MLFLOW_EXPERIMENT_ID`** environment variable
5. the **Default experiment** (id `0`) if nothing above is set

### 🔁 Return value
`start_run()` returns an **`mlflow.ActiveRun`** object that works as a **context manager** —
that's why we use it with `with`:
```python
with mlflow.start_run() as run:      # ActiveRun; auto-ends at the end of the block
    mlflow.log_metric("acc", 0.9)
```
Using `with` means you **don't** have to call `end_run()` yourself — it ends automatically,
even if an error happens. (Without `with`, you must call `end_run()` manually — see below.)

---

## 2. `mlflow.end_run(status="FINISHED")` — end the active run
- Ends the run that's currently active.
- **Only needed when you did NOT use `with`.** The `with mlflow.start_run():` form calls it for you.
- `status` can be `"FINISHED"` (default), `"FAILED"`, or `"KILLED"`.

## 3. `mlflow.active_run()` — the run happening RIGHT NOW
- Returns the currently active **Run** object, or **`None`** if no run is active.
- Handy to grab the current run's id: `mlflow.active_run().info.run_id`.

## 4. `mlflow.last_active_run()` — the LAST run, even after it ended
- Returns the most recently active run — **even after it has finished** (after a `with` block).
- Perfect with **`autolog()`**: autolog opens/closes the run for you, so afterwards you use
  `last_active_run()` to get that run's id/details.

---

## 🧭 Which do I use?
| I want to... | Use |
|--------------|-----|
| Start a normal new run | `with mlflow.start_run(run_name=...):` |
| Continue logging to an old run | `start_run(run_id="...")` |
| A sub-run inside another run | `start_run(nested=True)` |
| Start/stop without `with` | `start_run()` … `end_run()` |
| Check if a run is active now | `active_run()` |
| Get details of the run I just finished | `last_active_run()` |

> 💡 **99% of the time** you'll just write `with mlflow.start_run(run_name="..."):` and log inside it.
> The others are for specific needs (resuming, nesting, manual control, post-run inspection).
