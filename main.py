import os
import random


def clear_console():
    os.system('cls')


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display.append("_")
print(display)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

guess = input("Guess a letter: ").lower()
word_len = len(chosen_word)

index = -1
for letter in chosen_word:
    index += 1
    if guess == letter:
        display[index] = letter
        print("Right")
    else:
        print("Wrong")

clear_console()
print(display)
