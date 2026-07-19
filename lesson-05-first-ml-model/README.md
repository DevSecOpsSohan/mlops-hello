# Lesson 05 — Train Your First ML Model 🎓

> Phase 0 graduation project. Train, evaluate, and save a real scikit-learn model.

---

## 🧪 Hands-on lab

**File:** [`train.py`](train.py) — trains a Logistic Regression classifier on the Iris dataset.

```bash
# from an activated venv, at the repo root:
python lesson-05-first-ml-model/train.py
```

**Output:**
```text
Test accuracy: 100.0%
Model saved to model.joblib
```

> `model.joblib` is a binary **model artifact** — it's git-ignored (`*.joblib`). We version models properly with DVC/MLflow later, not Git.

---

## 🧠 The core ML loop (never changes, even for deep learning / LLMs)

```text
Data → Split (train/test) → Train (fit) → Predict → Evaluate → Save
```

| Step | Code | Plain English |
|------|------|---------------|
| Load | `load_iris()` | 150 flowers: 4 measurements (X) + species (y) |
| Split | `train_test_split(test_size=0.2)` | 80% to learn from, 20% held back for the exam |
| Train | `model.fit(X_train, y_train)` | the model learns the pattern |
| Predict | `model.predict(X_test)` | guess species for unseen flowers |
| Evaluate | `accuracy_score(...)` | % of correct guesses |
| Save | `joblib.dump(model, ...)` | write the trained model to disk (the artifact) |

> 🔑 **Golden rule:** never test on data the model trained on — that's why we split.

---

## ❓ Interview Q&A

**Q: Why split data into train and test sets?**
> To measure performance on *unseen* data. Testing on training data would give a meaningless score — a model that just memorized would look perfect but fail in the real world.

**Q: What do `fit()` and `predict()` do?**
> `fit()` trains the model (it learns the pattern); `predict()` uses the trained model to produce outputs for new inputs.

**Q: What are features (X) and labels (y)?**
> Features are the inputs the model learns from; the label is the target it predicts.

**Q: What is `random_state` for?**
> It seeds the randomness (e.g. the split) so results are reproducible — same split every run. Supports the reproducibility pillar.

**Q: What is `model.joblib`, and why does it matter for MLOps?**
> It's the saved model artifact. MLOps takes that artifact and deploys, versions, monitors, and retrains it — everything around this script.

**Q: Would you expect 100% accuracy on a real project?**
> No — Iris is a tiny, clean, easily separable dataset. Real data is messy; expect 70–95%. The 100% here is legit (tested on unseen data), just an easy dataset.

---

_Part of my [MLOps learning journey](../README.md). 🎓 This completes Phase 0._
