import sqlite3

# Connect to the database
conn = sqlite3.connect('parking_ticket_data.db')
cursor = conn.cursor()

# Function to retrieve ticket information based on LicencePlate
def get_ticket_info(licence_plate):
    cursor.execute("""
        SELECT * FROM ParkingTickets WHERE LicencePlate = ?
    """, (licence_plate,))
    
    result = cursor.fetchall()
    
    if result:
        for row in result:
            print(f"TicketNumber: {row[0]}")
            print(f"LotNumber: {row[1]}")
            print(f"LicencePlate: {row[2]}")
            print(f"TotalFine: {row[3]}")
            print(f"IntakeTime: {row[4]}")
            print(f"ExpirationTime: {row[5]}")
            print("-" * 30)
    else:
        print("No tickets found for this LicencePlate.")

def check_time():
    # Get user input
    licence_plate = input("Enter your Licence Plate number: ")

    # Retrieve and display ticket information
    get_ticket_info(licence_plate)

    # Close the database connection
    conn.close()