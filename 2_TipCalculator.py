"""
Tip Calculator
by Wyatt Newell
6/28/2024
"""
import time

# print(f"\nWelcome to Tip Calculator by Wyatt Newell\n")
# time.sleep(2)
# user_name = input(f"Please enter your name: ")
# print(f"Hello, {user_name}! The program is about to begin.\n")
# time.sleep(2)

def main():
    # Find the initial amount from the user
    amount = input(f"Please insert the amount owed before tip: ")
    try:
        float(amount)
    except:
        print("Invalid value, please try again")
        main()
    
    # Determine Tip Percentage
    print(f"Select Tip Percentage or select Custom")
    print(f"1) 10%\n2) 15%\n3) 20%\n4) 22%\n5) Custom\n")
    tip_selection = input(f"Enter Selection: ")
    while tip_selection not in ["1", "2", "3", "4", "5"]:
        print(f"\nInvalid Selection")
        tip_selection = input(f"Enter Selection: ")
    if tip_selection == "1":
        tipped_amount = float(amount) * 00.10
        total_amount = float(amount) + float(tipped_amount)
        print(f"Your 10% tip for ${amount} is ${tipped_amount} for a total of ${total_amount}")
    elif tip_selection == "2":
        tipped_amount = float(amount) * 00.15
        total_amount = float(amount) + float(tipped_amount)
        print(f"Your 15% tip for ${amount} is ${tipped_amount} for a total of ${total_amount}")
    elif tip_selection == "3":
        tipped_amount = float(amount) * 00.20
        total_amount = float(amount) + float(tipped_amount)
        print(f"Your 20% tip for ${amount} is ${tipped_amount} for a total of ${total_amount}")
    elif tip_selection == "4":
        tipped_amount = float(amount) * 00.22
        total_amount = float(amount) + float(tipped_amount)
        print(f"Your 22% tip for ${amount} is ${tipped_amount} for a total of ${total_amount}")
    elif tip_selection == "5":
        tipped_amount = input(f"Insert your custom tip %")
        total_amount = float(amount) + float(tipped_amount)
        print(f"Your 22% tip for ${amount} is ${tipped_amount} for a total of ${total_amount}")        

    
    

main()