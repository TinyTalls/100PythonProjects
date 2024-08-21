import sqlite3
from datetime import datetime

def read_from_db():
    conn = sqlite3.connect('parking_ticket_data.db')  # Connect to the database
    cursor = conn.cursor()

    # Execute a query to retrieve all records
    cursor.execute('SELECT * FROM ParkingTickets')

    # Fetch all rows from the result of the query
    rows = cursor.fetchall()

    # Process and print the results
    print("Ticket Number | Lot Number | Licence Plate | Total Fine | Intake Time | Expiration Time")
    print("-" * 40)
    for row in rows:
        print(f"{row[0]:<13} | {row[1]:<10} | {row[2]:<14} | ${row[3]:<10.2f} | {row[4]:<20} | {row[5]:<20}")
    conn.close()  # Close the connection

def check_expired_tickets():
    # Connect to the SQLite database (replace 'your_database.db' with your database file)
    conn = sqlite3.connect('parking_ticket_data.db')
    cursor = conn.cursor()

    # Get the current date and time
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # SQL query to select tickets with ExpirationTime less than the current date and time
    query = '''SELECT * FROM ParkingTickets
            WHERE ExpirationTime < ? '''

    # Execute the query
    cursor.execute(query, (now,))

    # Fetch all rows that match the query
    expired_tickets = cursor.fetchall()

    # Print the expired tickets
    print("Ticket Number | Lot Number | Licence Plate | Total Fine | Intake Time          | Expiration Time     ")
    print("-" * 60)
    for row in expired_tickets:
        print(f"{row[0]:<13} | {row[1]:<10} | {row[2]:<14} | ${row[3]:<10.2f} | {row[4]:<20} | {row[5]:<20}")

    # Close the connection
    conn.close()

def save_to_db(LotNumber, LicencePlate, TotalFine, IntakeTime, ExpirationTime):
    conn = sqlite3.connect('parking_ticket_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS ParkingTickets (TicketNumber INTEGER PRIMARY KEY AUTOINCREMENT, LotNumber INT NOT NULL, LicencePlate VARCHAR(20) NOT NULL, TotalFine DECIMAL(10, 2) NOT NULL, IntakeTime TIMESTAMP NOT NULL, ExpirationTime TIMESTAMP NOT NULL)''')
    cursor.execute('INSERT INTO ParkingTickets (LotNumber, LicencePlate, TotalFine, IntakeTime, ExpirationTime) VALUES (?, ?, ?, ?, ?)',
                   (LotNumber, LicencePlate, TotalFine, IntakeTime, ExpirationTime))
    conn.commit()
    conn.close()
