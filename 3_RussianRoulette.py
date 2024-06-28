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

# The Gun
def russianRoulette():
    global turn
    global chambers
    global loaded_chamber
    global current_chamber
    global game_over
    chambers = [1, 2, 3, 4, 5, 6]
    loaded_chamber = []
    current_chamber = []
    game_over = 0
    print(f"A robotic hand reaches out and takes the revolver, loading a single bullet. Then it spins the gun's cylinder.\n")
    time.sleep(1)
    print(f"\n* swish *\n")
    time.sleep(1)
    loaded_chamber = random.randrange(1,6)
    print(f"The revolver's locks its chamber into place.")
    # DEBUG - loaded_chamber reveal
    print(f"DEBUG - loaded_chamber = {loaded_chamber}")
    while game_over == 0:
        if turn == 1:


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