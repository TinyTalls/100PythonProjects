"""
Wy-Park.py
by Wyatt Newell
8/9/2024

After going to the beach with my girlfriend, I took notice of the parking payment computers. 
As opposed to the old coin operated parking meters, this program had users input their licence plate number, then through cash or card pay hourly for parking.
A ticket prints for the user, detailing the alloted parking time and car information. There was an online mobile option to pay as well.
The parking attendents had handheld computers, and could verify if the parked cars were legal.

I don't intend for this program to be too terribly complex, but I haven't coded in a moment and need to warm back up
"""
from datetime import datetime, date
import time


def print_current_time():
    """
    print_current_time = returns a string with the current date, then time underneath.
    """
    current_time = datetime.now().strftime("%I:%M:%S %p")
    current_date = date.today().strftime("%B %d, %Y")
    current_time_and_date = print(current_date + f"\n" + current_time)
    return current_time_and_date


def intro():
    print("\n" + "+" * 50)
    print(" Wy-Park ".center(50))
    print(" The Future of Parking ".center(50) + "\n" + "+" * 50 + "\n")
intro()