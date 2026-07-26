# Project 1 — Number Guessing Game 🎲

Part of my **Python Solidification Bootcamp** (fixing "vanishing" Python via rebuild-from-memory).

## What it does
Computer holds a secret number (7). User keeps guessing in a loop; the program says
"too low" / "too high" until correct, then reports how many guesses it took.

## How to run
```bash
python guessing_game.py
```

## Python skills drilled
- `while True:` infinite loop + `break`
- `input()` + `int()` conversion
- `if / elif` comparison logic
- f-strings: `f"You took {attempts} guesses"`
- a counter with `attempts += 1` (placed once, after input, so every guess counts)

## What I learned / what was hard
- **Bug I fixed:** `input()` must be *inside* the loop, or it only asks once.
- **Bug I fixed:** `break` only on the correct guess — not on wrong ones.
- **Bug I fixed:** count every guess in ONE place (after input), not per branch — otherwise the winning guess isn't counted.
- **Gotcha:** saved as `.py.txt` at first — Python files must end in `.py`.

## 🔁 Rebuild-from-memory test
- [ ] Rebuild this from a blank file, no looking (target: ~2 weekends from now). That's what makes it permanent.
