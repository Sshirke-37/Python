#Dictionary CRUD of PRODUCTS
# Main dictionary to store product records
products = {}

# Predefined product categories
Product_Categories = ['Electronics', 'Home Appliances', 'Clothing', 'Books', 'Groceries']

# Function to add a new product
def add_product():
    prod_code = input("Enter product code (alphanumeric only): ").upper()
    if not prod_code.isalnum():
        print("Error: Product code must contain only letters and numbers.")
        return
    if prod_code in products:
        print("Error: This product code already exists. Please enter a unique code.")
        return

    stock = int(input("Enter stock in hand (numeric): "))
    if stock < 0:
        print("Error: Stock must be a non-negative number.")
        return

    print("Available Categories:")
    for items in Product_Categories:
        print(f" - {items}")
    category = input("Enter product category: ")
    if category not in Product_Categories:
        print("Error: Invalid category. Please choose from the predefined list.")
        return

    price = float(input("Enter price (numeric): "))
    if price < 0:
        print("Error: Price must be a non-negative number.")
        return

    products[prod_code] = {
        'stock_in_hand': stock,
        'product_category': category,
        'price': price
    }
    print(f"Product '{prod_code}' added successfully!")

# Function to update an existing product
def update_product():
    prod_code = input("Enter the product code to update: ").upper()
    if prod_code not in products:
        print(f"Error: Product code '{prod_code}' not found.")
        return

    print("\nWhat would you like to update?")
    print("a. Stock in hand")
    print("b. Product Category")
    print("c. Price")
    update_choice = input("Enter your choice (a/b/c): ")

    if update_choice == 'a':
        new_stock = int(input("Enter new stock in hand: "))
        if new_stock < 0:
            print("Error: Stock must be a non-negative number.")
        else:
            products[prod_code]['stock_in_hand'] = new_stock
            print(f"Stock for '{prod_code}' updated successfully.")
    elif update_choice == 'b':
        print("Available Categories:")
        for items in Product_Categories:
            print(f" - {items}")
        new_category = input("Enter new product category: ")
        if new_category not in Product_Categories:
            print("Error: Invalid category. Please choose from the predefined list.")
        else:
            products[prod_code]['product_category'] = new_category
            print(f"Category for '{prod_code}' updated successfully.")
    elif update_choice == 'c':
        new_price = float(input("Enter new price: "))
        if new_price < 0:
            print("Error: Price must be a non-negative number.")
        else:
            products[prod_code]['price'] = new_price
            print(f"Price for '{prod_code}' updated successfully.")
    else:
        print("Invalid update choice. No changes were made.")

# Function to delete a product
def delete_product():
    prod_code = input("Enter the product code to delete: ").upper()
    if prod_code in products:
        del products[prod_code]
        print(f"Product '{prod_code}' deleted successfully.")
    else:
        print(f"Error: Product code '{prod_code}' not found.")

# Function to search for a product
def search_product():
    prod_code = input("Enter the product code to search: ").upper()
    if prod_code in products:
        print("--- Product Details ---")
        print(f"Product Code: {prod_code}")
        for key, value in products[prod_code].items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    else:
        print(f"Error: Product code '{prod_code}' not found.")

# Function to display all products
def display_all_products():
    if not products:
        print("The product inventory is empty.")
    else:
        print("--- All Product Records ---")
        for prod_code, details in products.items():
            print(f"\nProduct Code: {prod_code}")
            for key, value in details.items():
                print(f"  {key.replace('_', ' ').title()}: {value}")

# Main menu loop
def main_menu():
    while True:
        print("\n!--- Product Inventory Management ---!")
        print("1. Add a new product")
        print("2. Update an existing product")
        print("3. Delete a product")
        print("4. Search for a product")
        print("5. Display all products")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_product()
        elif choice == '2':
            update_product()
        elif choice == '3':
            delete_product()
        elif choice == '4':
            search_product()
        elif choice == '5':
            display_all_products()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
