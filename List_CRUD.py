# List CRUD without creation option
# Predefined List
my_list = ["apple", "banana", "cherry"]

while True:
    print("\n--- List Menu ---")
    print("1. Add an element at the beginning of the list")
    print("2. Add an element at the end of the list")
    print("3. Remove element")
    print("4. Display all the elements of the list")
    print("5. Exit")
    choice = input("Enter your choice (1–5): ")

    if not isinstance(my_list, list):
        print("List is not initialized.")
        continue

    if choice == '1':
        item = input("Enter element to add at beginning: ")
        my_list.insert(0, item)
    elif choice == '2':
        item = input("Enter element to add at end: ")
        my_list.append(item)
    elif choice == '3':
        item = input("Enter element to remove: ")
        if item in my_list:
            my_list.remove(item)
            print(f"'{item}' removed.")
        else:
            print(f"'{item}' not found in the list.")
    elif choice == '4':
        if my_list:
            print("List contents:", my_list)
        else:
            print("List is empty.")
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
