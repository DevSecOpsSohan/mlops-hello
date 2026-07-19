# Lesson 01 — What is MLOps?

> Concept lesson. No code — this is about understanding *what* MLOps is and *why* it exists.

---

## 🧠 Key concepts

**MLOps = Machine Learning Operations.** It combines **software engineering** and **DevOps** practices to streamline deploying ML models to production — and keeping them healthy after deployment.

> **ML vs MLOps:** Machine Learning is *building* the model (algorithm + data). MLOps is everything *around* it — deploying, versioning, monitoring, and retraining it in production.

### The 4 Pillars
1. **Reproducibility** — rebuild the exact model, data & environment anytime.
2. **Automation (CI/CD/CT)** — pipelines run with no manual steps.
3. **Monitoring** — detect when the model breaks or drifts.
4. **Governance** — version everything, roll back anything.

### The MLOps Lifecycle (7 stages)
1. Requirement Gathering
2. EDA (Exploratory Data Analysis)
3. Feature Engineering
4. Model Building
5. Hyperparameter Tuning
6. Model Deployment
7. Retraining

### Model Degradation & Data Drift
A model's performance slowly **degrades in production** over time — not because it changes, but because the **real-world data changes** (new behaviour, trends, prices) while the model stays frozen on old data. This mismatch is **data drift**.
**Fix:** an automated **retraining pipeline** (CI/CD/CT) that re-runs stages 2 → 6 when triggered by a schedule or by monitoring detecting a drop.

---

## ❓ Interview Q&A (what I can now answer)

**Q: What is MLOps in one sentence?**
> DevOps applied to machine learning — practices to reliably deploy, monitor, version, and retrain ML models in production.

**Q: Difference between ML and MLOps?**
> ML builds the model; MLOps takes it to production and keeps it healthy.

**Q: Name the 4 pillars.**
> Reproducibility, Automation, Monitoring, Governance.

**Q: Why does a model degrade over time?**
> The world's data changes while the model stays frozen on old data → data drift → worse predictions. Fixed by retraining.

---

_Part of my [MLOps learning journey](../README.md)._
