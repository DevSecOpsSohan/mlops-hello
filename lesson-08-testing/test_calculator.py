from calculator_funcs import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6      # BLANK 1: what should 10 - 4 be?

def test_multiply():
    assert multiply(3, 5) == 15

def test_divide():
    assert divide(10, 2) == 5        # BLANK 2: what should 10 / 2 be?

def test_divide_by_zero():
    # divide returns a message instead of crashing — assert we get that message
    assert divide(10, 0) == "Error: cannot divide by zero!"      # BLANK 3: the exact error text (check calculator_funcs.py!)
