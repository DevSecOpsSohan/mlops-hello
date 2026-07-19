# Lesson 04 — Virtual Environments & Dependencies

> Isolate a project's packages and record them so anyone can rebuild the exact setup. This is the **Reproducibility pillar** in practice.

---

## 🧪 Hands-on lab

**File:** [`requirements.txt`](requirements.txt) — the frozen list of exact package versions for this project.

### The commands I ran

```powershell
# 1. Create a virtual environment (project's private package box)
python -m venv .venv

# 2. Activate it (Windows PowerShell) — prompt shows (.venv)
.\.venv\Scripts\Activate.ps1

# 3. Install a package INTO the box (global Python stays clean)
pip install scikit-learn

# 4. Freeze exact versions into a recipe file
pip freeze > requirements.txt

# 5. Leave the environment when done
deactivate
```

### How anyone rebuilds my exact environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt      # installs the EXACT versions I froze
```

> ⚠️ If activation fails with "running scripts is disabled," run once:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

---

## 🧠 Key concepts

- **venv isolates, requirements.txt records.**
- Each project gets its own `.venv` so package versions never clash between projects.
- **Never commit `.venv/`** — it's large, machine-specific, and rebuildable. Commit `requirements.txt` (the recipe) instead. `.venv/` is in `.gitignore`.
- `pip freeze` captures **exact versions** (`scikit-learn==1.5.1`) so the environment is reproducible anywhere.

---

## ❓ Interview Q&A

**Q: What is a virtual environment and why use one?**
> An isolated Python environment per project, so each has its own package versions without clashing. Prevents dependency conflicts and makes projects reproducible.

**Q: What is `requirements.txt`?**
> A file listing a project's exact package versions. `pip install -r requirements.txt` recreates the same environment — supporting the reproducibility pillar.

**Q: Why not commit the `.venv` folder?**
> It's large, machine-specific, and rebuildable. We commit the recipe (`requirements.txt`), not the cooked result.

**Q: How does this relate to MLOps?**
> Reproducibility is a core pillar. venv + requirements.txt (and later Docker) ensure the model can be rebuilt identically in dev, CI, and production.

---

_Part of my [MLOps learning journey](../README.md)._
