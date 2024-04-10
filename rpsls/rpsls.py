# TODO: Develop a console-based Rock Paper Scissors Lizard Spock game in Python
# Game should be modular, allowing for easy updates or rule changes
# Implement game rules:
# - Scissors decapitate lizard
# - Scissors cuts paper
# - Paper covers rock
# - Rock crushes lizard
# - Lizard poisons Spock
# - Spock smashes scissors
# - Lizard eats paper
# - Paper disproves Spock
# - Spock vaporizes rock
# - Rock crushes scissors
# Include user input for selecting options and display game results

import random

# Define global variables
# Define dictionery of game options
options = {
    1: "rock",
    2: "paper",
    3: "scissors",
    4: "lizard",
    5: "spock"
}

# Define dictionery of game rules
rules = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['spock', 'paper'],
    'spock': ['scissors', 'rock']
}

# Define dictionary of game results
results = {
    'win': {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock']
    },
    'lose': {
        'rock': ['paper', 'spock'],
        'paper': ['scissors', 'lizard'],
        'scissors': ['rock', 'spock'],
        'lizard': ['rock', 'scissors'],
        'spock': ['paper', 'lizard']
    },
    'tie': {
        'rock': ['rock'],
        'paper': ['paper'],
        'scissors': ['scissors'],
        'lizard': ['lizard'],
        'spock': ['spock']
    }
}

# Define function to get user input
def get_user_input():
    user_choice = input('Enter your choice (rock, paper, scissors, lizard, spock): ').lower()
    return user_choice

# Define function to get computer input
def get_computer_input():
    computer_choice = random.choice(options)
    return computer_choice

# Define function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif computer_choice in rules[user_choice]:
        return 'win'
    else:
        return 'lose'

# Define function to display the results
def display_results(user_choice, computer_choice, result):
    if result == 'tie':
        print(f'It\'s a tie! You both chose {user_choice}.')
    elif result == 'win':
        print(f'You win! {user_choice} beats {computer_choice}.')
    else:
        print(f'You lose! {computer_choice} beats {user_choice}.')

# Define function to play the game
def play_game():
    user_choice = get_user_input()
    computer_choice = get_computer_input()
    result = determine_winner(user_choice, computer_choice)
    display_results(user_choice, computer_choice, result)

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break



""" def rpsls():
    # Define the rules of the game
    rules = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock']
    }

    # Define the options for the game
    options = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    # Get the user's choice
    user_choice = input('Enter your choice (rock, paper, scissors, lizard, spock): ').lower()

    # Check if the user's choice is valid
    if user_choice not in options:
        print('Invalid choice. Please enter a valid choice.')
        return

    # Get the computer's choice
    computer_choice = random.choice(options)

    # Determine the winner
    if user_choice == computer_choice:
        print(f'It\'s a tie! You both chose {user_choice}.')
    elif computer_choice in rules[user_choice]:
        print(f'You win! {user_choice} beats {computer_choice}.')
    else:
        print(f'You lose! {computer_choice} beats {user_choice}.')

# Call the rpsls function
rpsls() """

