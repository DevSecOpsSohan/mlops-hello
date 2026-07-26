# Project 2 — To-Do List (terminal) 📝

Part of my **Python Solidification Bootcamp** (fixing "vanishing" Python via rebuild-from-memory).

## What it does
A menu that loops. The user can add tasks, view them (numbered), or quit.
Tasks are stored in a **list**.

## How to run
```bash
python todo.py
```

## Python skills drilled
- `lists` — storing many items in one variable (`tasks = []`)
- `.append()` — adding an item to a list
- `for` loops — going through every item in a list
- `enumerate(tasks, start=1)` — get a counter AND the item each loop
- **tuple unpacking** — `for i, task in ...` (two variables catch the two things enumerate gives)
- f-strings + the menu pattern (`while True` + `break`, reused from Project 1)

## What I learned / what was hard
- **Bug I fixed:** `exit` doesn't leave a loop — the keyword is `break` (same as the guessing game).
- **Bug I fixed:** `enumerate` gives TWO things per loop, so I needed TWO variables (`for i, task`), otherwise `task` held the whole tuple `(1, 'Buy Milk')`.
- **Rule that stuck:** however many things a loop hands you, that's how many variables you need to catch them. (This shows up in ML too: `for X, y in ...`.)

## 🔁 Rebuild-from-memory test
- [ ] Rebuild this from a blank file, no looking (~2 weekends from now). That's what makes it permanent.

## Possible upgrades (future)
- Option 4: remove a task (`.remove()`)
- Save tasks to a file so they survive after quitting
