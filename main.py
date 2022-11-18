import os
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display.append("_")
print(display)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()
    index = 0
    for letter in chosen_word:
        if guess == letter:
            display[index] = letter
        index += 1
    print(display)

if "_" not in display:
    print("You win!")
    game_over = True

