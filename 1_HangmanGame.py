"""
Hangman Game
100 Python Projects
by Wyatt Newell
6/27/2024
"""

import random, time

# Initialize Game
print("\nHangman by Wyatt Newell\n")
player_name = input(f"Please enter your name: ")
print(f"Hello, {player_name}! Good luck, and don't get hanged!")
time.sleep(2)
print(f"The game is about to begin!")
time.sleep(3)

def main():
    global count
    global display
    global already_guessed 
    global length
    global play_game
    words_to_guess = ["abundance", "benevolent", "contradict", "diligent", "eloquent", "fortitude", 
                      "gracious", "hinder", "illustrate", "jovial", "knowledgeable", 
                      "meticulous", "nostalgia", "perservere", "resilient"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""