# Lesson 03 — Python Fundamentals

> Functions, lists, dicts, and the 4 core loop patterns — written the professional way.

---

## 🧪 Hands-on labs

| File | What it does |
|------|--------------|
| [`model_report.py`](model_report.py) | Prints a model report (best/avg/worst) and a deploy decision from a list of scores. |
| [`experiment_tracker.py`](experiment_tracker.py) | Finds the best run in a dict of experiments, checks a threshold with a default parameter. |
| [`model_registry.py`](model_registry.py) | A mini model registry: counts deployable models, lists their names, finds the worst. |
| [`lists_dicts_drills.py`](lists_dicts_drills.py) | Fluency drills for lists & dicts (the 4 core patterns). |

Run any of them:
```bash
python lesson-03-python-fundamentals/model_registry.py
```

**Example output (`model_registry.py`):**
```text
Total models:       4
Deployable (>=90%): 2
Deployable names:   ['random_forest', 'xgboost']
Worst model:        neural_net (71.0%)
```

---

## 🧠 The 4 core loop patterns (cover ~90% of data wrangling)

1. **COUNT** → `count = 0` → `count += 1` on match → return an int
2. **FILTER/COLLECT** → `result = []` → `result.append(x)` → return the list *after* the loop
3. **FIND MAX/MIN** → track a `best_score`/`best_name`, update on comparison
4. **TRANSFORM** → build a new list where each item is converted

> 🔑 Golden rule I learned: **functions return, the `main` block prints.** A function that `print`s can only print; one that `return`s can be reused (logged, fed to an API, etc.).

---

## ❓ Interview Q&A

**Q: List vs dictionary — difference and when to use each?**
> A list is an ordered collection accessed by position; a dict stores key→value pairs accessed by key. Lists for sequences (scores), dicts for named things (a config, model→accuracy).

**Q: What does `if __name__ == "__main__":` do?**
> Code inside runs only when the file is executed directly, not when imported as a module. Keeps scripts reusable.

**Q: What's the trap with `return` inside a loop?**
> `return` exits the whole function immediately, so you get only the first match. To collect all matches, append to a list and return *after* the loop.

**Q: What does `scores[-1]` return?**
> The last item of the list (negative indexing counts from the end).

---

_Part of my [MLOps learning journey](../README.md)._
