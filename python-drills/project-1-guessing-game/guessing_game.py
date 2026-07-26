secret_number = 7
attempts = 0

while True:
    number = int(input("Enter the number: "))   # ← inside the loop now
    attempts += 1
    if number == secret_number:
        print(f"correct! You took {attempts} guesses")
        break                                    # ← break ONLY here
    if number < secret_number:
        print("too low")                  # ← no break
    if number > secret_number:
        print("too high")                        # ← no break