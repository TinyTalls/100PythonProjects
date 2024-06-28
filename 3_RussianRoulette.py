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
print("\nRussian Roulette by Wyatt Newell\n")
player_name = input(f"Please enter your name: ")
print(f"Hello, {player_name}! Good luck, and don't get shot!")
time.sleep(2)
print(f"The game is about to begin!")
input(f"Press Enter to Start")
time.sleep(3)

def coin_flip_game():
    print(f"\nYou find yourself in a dark room sitting at a small wooden table. There's a revolver and a bullet."
            "\nFrom the darkness a robotic man leans his monitor face forward and asks with a pixel grin."
            "\n\n'Heads or Tails?'")
    time.sleep(1)
    print(f"1) Heads"
            "\n2) Tails\n")
    coin_flip_choice = input(f"Enter Selection: ")
    while coin_flip_choice not in ["1", "2"]:
        print(f"'ERROR' the computer monitor reads, 'Heads or Tails.' its speaker moans.")
        time.sleep(1)
        print(f"1) Heads"
            "\n2) Tails\n")
        coin_flip_choice = input(f"Enter Selection: ")
    print(f"A pixel hand holding a coin appears on the monitor. It flicks the coin with its thumb, flipping in virtual air.")
    coin_flip = random.randint(1,2)
    time.sleep(1)
    print(f"\n* swish *\n")
    time.sleep(1)
    print(f"The pixel hand catches the coin! Another hand appears, and the coin is flipped into it.")
    time.sleep(1)
    print(f"The palm opens...")
    if coin_flip == 1:
        print(f"Heads!")
    elif coin_flip == 2:
        print(f"Tails!")
    if coin_flip == 1 and coin_flip_choice == "1" or coin_flip == 2 and coin_flip_choice == "2":
        print(f"You win!")
        return True
    elif coin_flip == 1 and coin_flip_choice == "2" or coin_flip == 2 and coin_flip_choice == "1":
        print(f"You lose!")
        return False 



# Main Game
def main():
    if coin_flip_game() == True:
        print(f"Player Goes First")
    elif coin_flip_game() == False:
        print(f"Computer Goes First")
    
main()