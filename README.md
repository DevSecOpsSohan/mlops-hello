# 🚀 MLOps — Beginner to Advanced (my learning journey)

Hi, I'm **Sohan** 👋 — this repo documents my hands-on journey to becoming an **MLOps / DevOps engineer**, one weekend at a time.

Every lesson lives in its own folder with:
- 🧪 a **hands-on lab** (real, runnable Python code), and
- ❓ a **questions & answers** file (interview-style concepts I mastered that week).

I'm learning in public — follow along, or use it as a roadmap for your own start. ⭐ the repo if it helps you!

---

## 📚 Lessons

| # | Lesson | What I built / learned | Folder |
|---|--------|------------------------|--------|
| 01 | **What is MLOps?** | The 4 pillars, MLOps lifecycle (7 stages), model degradation & retraining | [`lesson-01-what-is-mlops/`](lesson-01-what-is-mlops/) |
| 02 | **Python + Git Workflow** | The `add → commit → push` loop, `.gitignore`, SSH to GitHub | [`lesson-02-python-git-workflow/`](lesson-02-python-git-workflow/) |
| 03 | **Python Fundamentals** | Functions, lists & dicts, the 4 core loop patterns, clean code | [`lesson-03-python-fundamentals/`](lesson-03-python-fundamentals/) |
| 04 | **Virtual Environments** | `venv`, `pip`, `requirements.txt` — reproducibility in practice | [`lesson-04-virtual-environments/`](lesson-04-virtual-environments/) |
| 05 | **First ML Model** 🎓 | Trained/evaluated/saved a scikit-learn model (train/test split, `fit`/`predict`) | [`lesson-05-first-ml-model/`](lesson-05-first-ml-model/) |

_More lessons added every weekend._

---

## 🧭 The 4 Pillars of MLOps (my north star)

1. **Reproducibility** — rebuild the exact model, data & environment anytime.
2. **Automation (CI/CD/CT)** — pipelines run with no manual steps.
3. **Monitoring** — detect when the model breaks or drifts.
4. **Governance** — version everything, roll back anything.

---

## 🛠️ How to run any lab

```bash
# clone the repo
git clone git@github.com:DevSecOpsSohan/mlops-hello.git
cd mlops-hello

# (from Lesson 04 onward) set up the environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1              # Windows
pip install -r lesson-04-virtual-environments/requirements.txt

# run any lesson's lab, e.g.
python lesson-03-python-fundamentals/model_registry.py
python lesson-05-first-ml-model/train.py
```

---

## 📈 Progress

- ✅ **Phase 0 — Prerequisites: COMPLETE** 🎓 (Lessons 01–05 — Python, Git, environments, and a trained ML model)
- ⬜ Phase 1 — Software Engineering Foundations for ML
- ⬜ Phase 2 — Core MLOps Tooling (MLflow, DVC)
- ⬜ Phase 3 — CI/CD & Automation
- ⬜ Phase 4 — Deployment & Orchestration (Docker, Kubernetes, Airflow)
- ⬜ Phase 5 — Monitoring & Production ML
- ⬜ Phase 6 — Advanced & Specialization (LLMOps)

---

_Learning MLOps beginner → advanced. One lesson every weekend. Consistency > intensity._ 💪
