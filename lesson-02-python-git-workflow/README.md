# Lesson 02 — Python + Git Workflow

> The core developer loop every MLOps engineer uses daily.

---

## 🧪 Hands-on lab

**File:** [`hello.py`](hello.py) — a tiny Python script with a `greet()` function.

```bash
python lesson-02-python-git-workflow/hello.py
```

**Output:**
```text
Hello, Sohan! Welcome to MLOps.
```

### The Git loop I practiced
```bash
git add hello.py          # stage the change
git commit -m "message"   # save a snapshot LOCALLY
git push                  # upload to GitHub (remote)
```

---

## 🧠 Key concepts

- Git's flow: **working directory → staging (`add`) → local repo (`commit`) → GitHub (`push`)**.
- **`.gitignore`** tells Git which files to never commit (secrets, data, temp files).
- Connected the local repo to GitHub over **SSH**.

---

## ❓ Interview Q&A

**Q: Difference between Git and GitHub?**
> Git is the version-control tool that runs locally. GitHub is a cloud service that hosts Git repositories for sharing/collaboration.

**Q: Where does `git commit` save to — local or remote?**
> Local repository. Nothing goes to the server until `git push`.

**Q: What does `git add` do?**
> Moves changes to the staging area — "these are the changes I want to save."

**Q: Why use `.gitignore`? Name something you should never commit.**
> To keep unwanted files out of the repo. Never commit secrets (`.env`, API keys) or large data/virtual-env folders.

---

_Part of my [MLOps learning journey](../README.md)._
