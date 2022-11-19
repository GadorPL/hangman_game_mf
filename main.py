import os
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives = 6
wrong_guesses = []

display = []
for letter in chosen_word:
    display.append("_")
print(f"{' '.join(display)}")
# Testing code
print(f'Pssst, the solution is {chosen_word}.')


game_over = False

while not game_over:
    print(stages[lives])
    if len(wrong_guesses) > 0:
        print(f"Wrong guesses: {' '.join(wrong_guesses)}")
    guess = input("Guess a letter: ").lower()
    index = 0
    for letter in chosen_word:
        if guess == letter:
            display[index] = letter
        index += 1
    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        lives -= 1
        wrong_guesses.append(guess)
        if lives == 0:
            print("You lost.")
            game_over = True

if "_" not in display:
    print("You win!")
    game_over = True

