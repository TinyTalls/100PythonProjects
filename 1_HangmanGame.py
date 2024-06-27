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
    global word
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

def play_loop():
    global play_game
    play_game = input("Would you like to play again?\n 1 = Yes, 2 = No\n Enter Selection: ")
    while play_game not in ["1", "2"]:
        play_game = input("Would you like to play again?\n 1 = Yes, 2 = No\n Enter Selection: ")
    if play_game == "1":
        main()
    elif play_game == "2":
        print("Thank you for playing Hangman, come back soon!")
        exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input(f"The Hangman's word is: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid input, try a letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word=word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    elif guess in already_guessed:
        print("Try another letter.\n")
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     |\n"
                 "  |     |\n"
                 "  |     O\n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")


            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "  |     \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    elif count != limit:
        hangman()
main()
hangman()