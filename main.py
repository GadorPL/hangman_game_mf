import random
from art import *
from words import *


chosen_word = random.choice(word_list)
lives = 6
previous_choices = []

print(logo, "\n")

display = []
for letter in chosen_word:
    display.append("_")
print(f"{' '.join(display)}")


game_over = False

while not game_over:
    print(stages[lives])
    guess = input("Guess a letter: ").lower()
    if guess in previous_choices:
        print(f"You've already guessed '{guess}'. Try again.")
    previous_choices.append(guess)
    index = 0
    for letter in chosen_word:
        if guess == letter:
            display[index] = letter
        index += 1
    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        print(f"'{guess}' is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("You lost.")
            game_over = True
    elif "_" not in display:
        print("You win!")
        game_over = True



