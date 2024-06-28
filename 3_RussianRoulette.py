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
input(f"Press Enter to Start.")
time.sleep(3)

