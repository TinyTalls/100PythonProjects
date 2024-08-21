import time, sqlite3, wy_park_db
from datetime import datetime


def parking_control(): 
    time.sleep(2)
    while True:
        print(f"Parking Control".center(50))
        print(f"Lot: coming soon".center(50) + "\n")

        menu_options = [
            "1. Check Active Tickets",
            "2. Check Expired Tickets",
            "3. Return to Main Menu",
        ]
    
        print(f"\n".join(menu_options))
        user_selection = input(f"\nEnter Selection: ")
        time.sleep(2)
        if user_selection not in ["1", "2", "3"]:
            print(f"Error: Invalid Selection")
            time.sleep(2)
        elif user_selection == "1":
            wy_park_db.read_from_db()
        elif user_selection == "2":
            wy_park_db.check_expired_tickets()
        else:
            break