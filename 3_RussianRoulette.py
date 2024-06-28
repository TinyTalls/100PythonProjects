"""
Russian Roulette
by Wyatt Newell
6/28/2024

https://en.wikipedia.org/wiki/Russian_roulette

It was my day off and I had extra time to do another project. 

This is Russian Roulette with some extra actions. A six chamber revolver is loaded with a single bullet, 
then the chamber is spun. Both the player and computer take turns firing the gun at themselves until the bullet is spent. 
In this variation, both player and computer will also have the option to shoot their opponent or spin the barrel.
Shooting the opponent has its consequences. If the gun fires blank at the opponent, the shooter must take another turn and shoot themselves.
The player and computer may only spin the barrel once per game. 
"""
import time, random

# Initialize Game
# print("\nRussian Roulette by Wyatt Newell\n")
# player_name = input(f"Please enter your name: ")
# print(f"Hello, {player_name}! Good luck, and don't get shot!")
# time.sleep(2)
# print(f"The game is about to begin!")
# input(f"Press Enter to Start")
# time.sleep(3)

# Coin flip to determine who goes first
def coin_flip_game():
    print(f"\nYou find yourself in a dark room sitting at a small wooden table. There's a revolver and a bullet."
            "\nFrom the darkness a robotic man leans his monitor face forward and asks with a pixel grin."
            "\n\n'Heads or Tails?'")
    time.sleep(1)

    # Player coin flip selection
    while True:
        print(f"1) Heads"
                "\n2) Tails\n")
        coin_flip_choice = input(f"Enter Selection: ")
        if coin_flip_choice in ["1", "2"]:
            break
        else:
            print(f"'ERROR' the computer monitor reads, 'Heads or Tails.' its speaker moans.")
            time.sleep(1)

    # The Flip
    print(f"A pixel hand holding a coin appears on the monitor. It flicks the coin with its thumb, flipping in virtual air.")
    coin_flip = random.randint(1,2)
    time.sleep(1)
    print(f"\n* swish *\n")
    time.sleep(1)
    print(f"The pixel hand catches the coin! Another hand appears, and the coin is flipped into it.")
    time.sleep(1)
    print(f"The palm opens...\n")
    time.sleep(1)

    # The Result
    print(f"Heads!" if coin_flip == 1 else f"Tails!")
    if (coin_flip == 1 and coin_flip_choice == "1") or (coin_flip == 2 and coin_flip_choice == "2"):
        print(f"\nYou win!")
        return True
    else:
        print(f"\nYou lose!")
        return False 

# The Game
def russianRoulette():
    global turn
    global chambers
    global loaded_chamber
    chambers = [1, 2, 3, 4, 5, 6]
    current_chamber = 1

    
    # The gun is loaded
    print(f"A robotic hand reaches out and takes the revolver, loading a single bullet. Then it spins the gun's cylinder.\n")
    loaded_chamber = random.choice(chambers)    
    time.sleep(1)
    print(f"\n* swish *\n")
    time.sleep(1)
    print(f"The revolver's locks its chamber into place.")

    # Basic Game Loop
    while True:

        # Player's Turn
        if turn == 1:

            # Player's Selection
            while True:
                print(f"With gun in hand, what will you do?\n"
                    "1) Shoot Self\n"
                    "2) Shoot Computer\n"
                    "3) Spin Barrel\n")
                player_choice = input(f"Enter Selection: ")
                if player_choice in ["1", "2", "3"]:
                    break
                else:
                    print(f"Invalid Selection.\n")

            # Selection Execution
            if player_choice == "1":
                print(f"The player takes the gun and aims it towards their head.")
            elif player_choice == "2":
                print(f"The player takes the gun and aims it towards the computer.")
            else: 
                print(f"The player spins the barrel")
                loaded_chamber = random.choice(chambers)
                current_chamber = 1
                time.sleep(1)
                print(f"\n* swish *\n")
                time.sleep(1)
                print(f"The revolver's locks its chamber into place.\n")
            
            time.sleep(2)

            if current_chamber == loaded_chamber:
                print(f"* click *")
                print(f"BOOM!")
                time.sleep(5)
                if player_choice == "2":
                    print("YOU WIN!")
                else:
                    print("GAME OVER")
                break
            else:
                print(f"* click *")
                time.sleep(1)
                current_chamber += 1
                if player_choice in ["1", "3"]:
                    print(f"The player hands the gun over to the computer.")
                    turn = 2
                else:
                    print(f"Well shit")
                    print(f"The player takes the gun and aims it towards their head.")
                    if current_chamber == loaded_chamber:
                        print(f"* click *")
                        print(f"BOOM!")
                        time.sleep(5)
                        print(f"GAME OVER")
                        break
                    else:
                        print(f"* click *")
                        time.sleep(1)
                        current_chamber += 1
                        print(f"The player hands the gun over to the computer.")
                        turn = 2

        # Computer's Turn
        elif turn == 2:

            # Computer's Choice
            computer_choice = random.randrange(1, 3)
            if computer_choice == 1:
                print(f"The computer takes the gun and aims it towards their head.")
            elif computer_choice == 2:
                print(f"The computer takes the gun and aims it at the player.")
            else:
                print(f"The computer spins the barrel")
                loaded_chamber = random.choice(chambers)
                current_chamber = 1
                time.sleep(1)
                print(f"\n* swish *\n")
                time.sleep(1)
                print(f"The revolver's locks its chamber into place.\n")

            
            time.sleep(2)

            if current_chamber == loaded_chamber:
                print(f"* click *")
                print(f"BOOM!")
                time.sleep(5)
                if computer_choice in [1, 3]:
                    print(f"YOU WIN!")
                    break
                else:
                    print(f"GAME OVER")
                    break
            else:
                print(f"* click *")
                time.sleep(1)
                print(f"...")
                current_chamber += 1
                if computer_choice in [1, 3]:
                    print(f"The computer hands the gun over to the player.")
                    turn = 1
                else:
                    print(f"The computer speaker cries, 'Oh Fuck")
                    if current_chamber == loaded_chamber:
                        print(f"* click *")
                        print(f"BOOM!")
                        time.sleep(5)
                        print(f"YOU WIN!")
                        break
                    else:
                        print(f"* click *")
                        time.sleep(1)
                        current_chamber += 1
                        print(f"The computer hands the gun over to the player.")
                        turn = 1
                    







# Main 
def main():
    global turn
    coin_flip_result = coin_flip_game()
    if coin_flip_result == True:
        print(f"Player Goes First")
        turn = 1
    elif coin_flip_result == False:
        turn = 2
        print(f"Computer Goes First")
    russianRoulette()
    
main()