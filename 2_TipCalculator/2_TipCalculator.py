"""
Tip Calculator
by Wyatt Newell
6/28/2024

Despite the ease of this project, I enjoyed working on it. It's a simple calculator, but I was able to practice dictionaries as well as try-except clauses. 
I want these projects to be bug-free. Therefore their simplicity now includes debugging, which makes for better programs. I don't know if I will return to this file,
but I forsee utilizing some of it for another program, such as a food ordering application. That would involve dividing main() into more functions.
"""
import time

print(f"\nWelcome to Tip Calculator by Wyatt Newell\n")
time.sleep(1)
user_name = input(f"Please enter your name: ")
print(f"Hello, {user_name}! The program is about to begin.\n")
time.sleep(1)

def main():
    # Find the initial amount from the user
    amount = input(f"Please insert the amount owed before tip: ")
    try:
        float(amount)
    except:
        print("Invalid value, please try again")
        main()
    
    # Input tip percentage
    print(f"Select Tip Percentage or select Custom")
    print(f"1) 10%\n2) 15%\n3) 20%\n4) 22%\n5) Custom\n")
    tip_selection = input(f"Enter Selection: ")
    while tip_selection not in ["1", "2", "3", "4", "5"]:
        print("\nInvalid Selection")
        tip_selection = input("Enter Selection: ")

    # Calculate tip and sum for total amount
    tip_percentages = {"1": 0.10, "2": 0.15, "3": 0.20, "4": 0.22}

    if tip_selection in tip_percentages:
        tipped_amount = float(amount) * tip_percentages[tip_selection]
        total_amount = float(amount) + tipped_amount
        time.sleep(1)
        print(f"\n{user_name}, your {int(tip_percentages[tip_selection] * 100)}% tip for ${amount} is ${tipped_amount:.2f} for a total of ${total_amount:.2f}\n")

    # Custom tip percent input     
    elif tip_selection == "5":
        while True:
            try:
                custom_tip_percentage = float(input("Insert your custom tip %: ")) / 100
                tipped_amount = float(amount) * custom_tip_percentage
                total_amount = float(amount) + tipped_amount
                time.sleep(1)
                print(f"\n{user_name}, your custom tip for ${amount} is ${tipped_amount:.2f} for a total of ${total_amount:.2f}\n")
                break
            except:
                print(f"\nInvalid Input. Please input a value from 1-100 without any symbols '%'\n")
                time.sleep(1)

    # Program Loop
    print(f"Would you like to find another tip percentage?")
    time.sleep(1)
    print(f"1) Yes\n2) No")
    loop_selection = input(f"Enter Selection: ")
    while loop_selection not in ["1", "2"]:
        print(f"Invalid Input.")
        loop_selection = input(f"Enter Selection: ")
    if loop_selection == "1":
        main()
    elif loop_selection == "2":
        print(f"\nThank you for using Tip Calculator, {user_name}!\nSee you soon!")
        exit()
    
main()