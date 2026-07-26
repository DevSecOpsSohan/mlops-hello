# Project 4 — Contact Book 📇

Final project of my **Python Solidification Bootcamp** — the graduation project.

## What it does
Stores contacts in a **dictionary** (`{name: phone}`). You can add contacts,
view all, look up a contact **by name** (instant), or look up **by number**
(reverse search), and quit.

## How to run
```bash
python contacts.py
```

## Python skills drilled
- **Dictionaries** — `{key: value}`; `contacts[name] = phone`
- Looking up by key — `contacts[search]` (instant)
- **Reverse lookup by value** — looping `contacts.items()` to find a match (advanced!)
- `if search in contacts:` — key-existence check (input validation)
- `.items()` + nested unpacking `for i, (name, phone) in enumerate(...)`
- `else` on the menu to handle invalid input

## What I learned / what was hard
- **Big idea:** in a dict, the KEY is what you search by. Names are keys, numbers are values. `if x in contacts` checks keys, not values.
- **Bug I fixed:** using `contacts[name]` instead of `contacts[search]` returns the wrong contact — use the variable that holds what you actually mean.
- **Bug I fixed:** storing `contacts[name] = name` broke the link — Add must always be `contacts[name] = phone`.
- **New concept I asked for myself:** a dictionary is one-way (fast key→value). To search by value (number → name) you must LOOP through every item. That's a "reverse lookup".
- **UX lesson:** good menu labels + an `else` for invalid input stop the user from getting confused.

## Why this matters for MLOps
Dictionaries are everywhere in ML/MLOps — model config, JSON API requests/responses,
feature dictionaries, hyperparameters. FastAPI request bodies arrive as dict-like data.

## 🔁 Rebuild-from-memory test
- [ ] Rebuild this from a blank file, no looking (~2 weekends from now).
