#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random


EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

print("Welcome to the Number Guessing Game!")
print("I'am thinking of a number between 1 and 100.")
number = random.randint(1, 100)

def choose_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  return (HARD_LEVEL_ATTEMPTS if level == 'hard' else EASY_LEVEL_ATTEMPTS)
  
def check_answer(guess, number):
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print(f"You got it! The answer was {guess}")
        exit()

def game():
    attempts = choose_difficulty()
    while attempts > 0:
        print(f"You have {attempts} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts -= 1
        check_answer(guess, number)
        if attempts > 0:
            print("Guess again")
        else:
            print(f"Pssst! The answer was {number}")

game()
