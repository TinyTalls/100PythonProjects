import time, wy_park_db, re
from datetime import datetime, timedelta, date

lot_number = 117

def add_hours_to_ticket(ticket_datetime, added_hours):
    """
    add_hours_to_ticket - takes the current ticket datetime and adds the corresponding hours, returning the new datetime
    """
    new_datetime = ticket_datetime + timedelta(hours=added_hours)
    return new_datetime

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
            wy_park_db.save_to_db(lot_number, _license_plate, _payment_owed, _intake_time, _ticket_experation,)
            print("Succesful!")
            break
        elif _user_confirmation == "2":
            break
        else:
            print("Invalid Selection.\n")
            time.sleep(2)