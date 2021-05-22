#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
print(logo)
lives = 5
def set_difficult(difficulty_level):
    global lives
    if difficulty_level == 'hard':
        lives = 5
    else:
        lives = 10
msg_flag = True # a flag to Guess again msg
print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
random_number = random.randint(1,100)
set_difficult(difficulty_level)
faild_to_guess = True
while faild_to_guess and lives >0:
    guess = int(input("Make a guess: "))
    if(guess == random_number):
        print(f"You got it! the answer was {random_number}")
        msg_flag = False
        faild_to_guess = False
    elif guess > random_number:
        print("Too high.")
    elif guess < random_number: 
        print("Too low.")
    lives -= 1
    if msg_flag == True:
        print("Guess again.")
if lives == 0:
    print(f"You lose, the number was {random_number}")
