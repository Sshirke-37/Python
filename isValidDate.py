from datetime import datetime

date_input = input("Enter a date (DD-MM-YYYY): ")

try:
    valid_date = datetime.strptime(date_input, "%d-%m-%Y")
    print("The date is valid.")
except ValueError:
    print("The date is invalid.")
