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
from datetime import datetime, date, timedelta
import time, re, sqlite3, parking_control

lot_number = 117




def save_to_db(LotNumber, LicencePlate, TotalFine, IntakeTime, ExpirationTime):
    conn = sqlite3.connect('parking_ticket_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS ParkingTickets (TicketNumber INTEGER PRIMARY KEY AUTOINCREMENT, LotNumber INT NOT NULL, LicencePlate VARCHAR(20) NOT NULL, TotalFine DECIMAL(10, 2) NOT NULL, IntakeTime TIMESTAMP NOT NULL, ExpirationTime TIMESTAMP NOT NULL)''')
    cursor.execute('INSERT INTO ParkingTickets (LotNumber, LicencePlate, TotalFine, IntakeTime, ExpirationTime) VALUES (?, ?, ?, ?, ?)',
                   (LotNumber, LicencePlate, TotalFine, IntakeTime, ExpirationTime))
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

def add_hours_to_ticket(ticket_datetime, added_hours):
    """
    add_hours_to_ticket - takes the current ticket datetime and adds the corresponding hours, returning the new datetime
    """
    new_datetime = ticket_datetime + timedelta(hours=added_hours)
    return new_datetime

def pay_for_parking():
    """
    pay_for_parking - The menu first function in Wy-Park. This will have the user input their license plate, desired parked hours, and confirm their payment at $2 an hour.
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
    _current_time = datetime.now()
    _ticket_experation = add_hours_to_ticket(_current_time, int(_time_selection))
    _experation_string = _ticket_experation.strftime("%Y-%m-%d %H:%M:%S")
    while True:
        print(("+" * 50) + "\n")
        print(f"Car: {_license_plate}".center(50))
        print(f"Hours: {_time_selection}".center(50)) 
        print(f"Total: ${_payment_owed}".center(50))
        print(f"Expires: {_experation_string}".center(50))
        print("\n")
        _user_confirmation = input(f"Confirm Information?\n1. Yes\n2. No\n")
        if _user_confirmation == "1":
            _cash_input = input(f"Press Enter to insert ${_payment_owed}.")
            _intake_time = datetime.now()
            save_to_db(lot_number, _license_plate, _payment_owed, _intake_time, _ticket_experation,)
            print("Succesful!")
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
        print(f"Lot: {lot_number}\n".center(50))
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
            parking_control.parking_control()
        elif user_selection == "5":
            break



main_menu()