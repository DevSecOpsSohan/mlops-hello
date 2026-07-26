tasks = []                       # our list of tasks (starts empty)

while True:
    print("\n--- TO-DO MENU ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Quit")
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)        # BLANK 1: which list method ADDS an item? (starts with app...)
        print("Task added!")

    elif choice == "2":
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    elif choice == "3":
        print("Goodbye!")
        break                # BLANK 2: which keyword EXITS the loop? (you used it in the game)

    else:
        print("Not a valid option, try again.")
