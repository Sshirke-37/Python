#List Crud
#Empty List
my_list = [ ]
while True:
    print("\n--- List Menu ---")
    print("1. Create a list")
    print("2. Add an element at the beginning of the list")
    print("3. Add an element at the end of the list")
    print("4. Remove element")
    print("5. Display all the elements of the list")
    print("6. Exit")
    choice = input("Enter your choice (1–6): ")

    if choice == '1':
        my_list = input("Enter elements separated by spaces: ").split()
    elif choice == '2':
        item = input("Enter element to add at beginning: ")
        my_list.insert(0, item)
    elif choice == '3':
        item = input("Enter element to add at end: ")
        my_list.append(item)
    elif choice == '4':
        item = input("Enter element to remove: ")
        if item in my_list:
            my_list.remove(item)
            print(f" '{item}' removed.")
        else:
            print(f" '{item}' not found in the list.")
    elif choice == '5':
        if my_list:
            print("List contents:", my_list)
        else:
                print("List is empty.")        
    elif choice == '6':
        print(" Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
