"""
Wy-Park.py
by Wyatt Newell
8/9/2024

After going to the beach with my girlfriend, I took notice of the parking payment computers. 
As opposed to the old coin operated parking meters, this program had users input their licence plate number, then through cash or card pay hourly for parking.
A ticket prints for the user, detailing the alloted parking time and car information. There was an online mobile option to pay as well.
The parking attendents had handheld computers, and could verify if the parked cars were legal.

I don't intend for this program to be too terribly complex, but I haven't coded in a moment and need to warm back up.
"""
from datetime import datetime, date
import time, re, sqlite3

def read_from_db():
    conn = sqlite3.connect('payment_data.db')  # Connect to the database
    cursor = conn.cursor()

    # Execute a query to retrieve all records
    cursor.execute('SELECT * FROM payments')

    # Fetch all rows from the result of the query
    rows = cursor.fetchall()

    # Process and print the results
    print("License Plate | Hours | Payment Owed")
    print("-" * 40)
    for row in rows:
        print(f"{row[0]:<15} | {row[1]:<5} | ${row[2]:.2f}")

    conn.close()  # Close the connection

def save_to_db(license_plate, time_selection, payment_owed):
    conn = sqlite3.connect('payment_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS payments
                      (license_plate TEXT, time_selection INTEGER, payment_owed REAL)''')
    cursor.execute('INSERT INTO payments (license_plate, time_selection, payment_owed) VALUES (?, ?, ?)',
                   (license_plate, time_selection, payment_owed))
    conn.commit()
    conn.close()

def validate_license_plate(license_plate):
    """
    validate_license_plate - Checks if the inputted license plate is within 8 characters and has no special characters
    """
    if len(license_plate) <= 0 or len(license_plate) > 8 or re.search(r'[^a-zA-Z0-9\s]', license_plate):
        raise ValueError("Error: Please enter valid License Plate Number") 
    else:
        return


def pay_for_parking():
    """
    pay_for_parking - The menu first function in Wy-Park. This will have the user input their license plate, desired parked hours, and confirm their payment at $2 an hour.
    TODO: save confirmed information.
    """
    # Step 1: Get the license plate information and validate it.
    while True:
        _license_plate = input(f"\nEnter License Plate Number: ")
        try:
            validate_license_plate(_license_plate)
            break
        except ValueError as e:
            print(e)
            time.sleep(2)

    # Step 2: Get the desired hours and validate it.
    while True:
        _time_selection = input(f"Enter Hours 1-12: ")
        if not _time_selection.isdigit() or not 1 <= int(_time_selection) <= 12:
            print("Error: Please enter hours within 1-12")
        else:
            break

    # Step 3: Calculate the payment owed with the desired hours, then confirm all the information with the user.
    _payment_owed = int(_time_selection) * 2
    while True:
        print(("+" * 50) + "\n")
        print(f"Car: {_license_plate}".center(50))
        print(f"Hours: {_time_selection}".center(50)) 
        print(f"Total: ${_payment_owed}".center(50))
        print("\n")
        _user_confirmation = input(f"Confirm Information?\n1. Yes\n2. No\n")
        if _user_confirmation == "1":
            _cash_input = input(f"Press Enter to insert ${_payment_owed}.")
            print("Succesful!")
            save_to_db(_license_plate, _time_selection, _payment_owed)
            break
        elif _user_confirmation == "2":
            break
        else:
            print("Invalid Selection.\n")
            time.sleep(2)


def intro():
    """
    intro = prints the Wy-Park intro
    """
    print("\n" + ("+" * 50) + "\n")
    print(" Wy-Park ".center(50))
    print(" The Future of Parking ".center(50) + "\n\n" + "+" * 50 + "\n")

def main_menu():
    while True:
        intro()
        print("Current Time".center(50))
        print(date.today().strftime("%B %d, %Y").center(50))
        print(datetime.now().strftime("%I:%M:%S %p").center(50) + "\n")

        menu_options = [
            "1. Pay for Parking",
            "2. Extend Parking",
            "3. Check Time",
            "4. Parking Control",
            "5. Exit"
        ]

        print("\n".join(menu_options))
        user_selection = input("\nEnter Selection: ")
        time.sleep(2)

        if user_selection not in ["1", "2", "3", "4", "5"]:
            print(f"\nError: Please input valid selection.\n")
            time.sleep(2)
        elif user_selection == "1":
            pay_for_parking()
        elif user_selection == "2":
            print("Extend Parking... Coming Soon!")
        elif user_selection == "3":
            print("Check Time... Coming Soon!")
        elif user_selection == "4":
            print("Parking Control... Coming Soon!")
            read_from_db()
        elif user_selection == "5":
            break



main_menu()