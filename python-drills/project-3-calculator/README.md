# Project 3 — Simple Calculator 🧮

Part of my **Python Solidification Bootcamp** (fixing "vanishing" Python via rebuild-from-memory).

## What it does
Asks for two numbers and an operation (+, -, *, /), then calls the matching
function and prints the result. Divide-by-zero is handled gracefully.

## How to run
```bash
python calculator.py
```

## Python skills drilled
- **Writing functions** with `def`, arguments (`a`, `b`), and **`return`** values
- Calling functions by their exact name
- `float(input(...))` for decimal numbers
- **Input validation** — guarding `divide` against division by zero
- `if / elif / else` to pick the right operation

## What I learned / what was hard
- **Bug I fixed:** `multiple` vs `multiply` → `NameError`. Function names must match exactly. Python even suggested the fix — READ the error message.
- **Bug I fixed:** `=` vs `==`. One `=` assigns, two `==` compares. An `if` always asks a question, so it needs `==`.
- **Bug I fixed:** stray space `num 1` → Python read it as two things.
- **Structure:** all functions belong together at the top; the interactive code goes below.
- **Big idea:** functions use their own parameter names (`a`, `b`) and are self-contained. `divide(num1, num2)` copies num1→a, num2→b automatically.

## Why this matters for MLOps
Every FastAPI endpoint is just a function that `return`s a value, and input
validation is exactly what Pydantic does for a model API. This project is the
bridge to Lesson 06 (serving a model with FastAPI).

## 🔁 Rebuild-from-memory test
- [ ] Rebuild this from a blank file, no looking (~2 weekends from now).
