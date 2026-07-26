# Project 4 — Contact Book
# Drills: dictionaries (key/value), lookup by key, and reverse lookup by value.

contacts = {}          # empty dictionary (note: {} not [])

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Look up a contact by name")
    print("4. Look up a contact by number")
    print("5. Quit")
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone        # name is the KEY, phone is the VALUE
        print("Contact added!")

    elif choice == "2":
        print("Your contacts:")
        for i, (name, phone) in enumerate(contacts.items(), start=1):
            print(f"{i}. {name}: {phone}")

    elif choice == "3":                           # look up by NAME (instant, native to dicts)
        search = input("Enter name to look up: ")
        if search in contacts:                    # check the key exists first
            print(f"{search}'s number is {contacts[search]}")
        else:
            print("Contact not found!")

    elif choice == "4":                           # look up by NUMBER (reverse — needs a loop)
        search = input("Enter number to look up: ")
        found = False
        for name, phone in contacts.items():      # check every contact
            if phone == search:                   # does this contact's number match?
                print(f"{search} belongs to {name}")
                found = True
        if not found:
            print("Contact not found!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:                                         # guide the user on bad input
        print("Invalid option, please choose 1-5.")
