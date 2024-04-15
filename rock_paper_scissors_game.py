# TODO: Develop a console-based Rock Paper Scissors game in Python
# Game should be modular, allowing for easy updates or rule changes
# Implement game rules:
# - Rock crushes scissors
# - Scissors cuts paper
# - Paper covers rock
# Include user input for selecting options and display game results
# Ask user to select an option and display the result
# Ask user if they want to play again
# If user selects 'yes', repeat the game
# If user selects 'no', exit the game

import random

# Define global variables
# Define dictionery of game options
options = {
    1: "rock",
    2: "paper",
    3: "scissors"
}

# Define dictionery of game rules
rules = {
    'rock': ['scissors'],
    'paper': ['rock'],
    'scissors': ['paper']
}

# Define dictionary of game results
results = {
    'win': {
        'rock': ['scissors'],
        'paper': ['rock'],
        'scissors': ['paper']
    },
    'lose': {
        'rock': ['paper'],
        'paper': ['scissors'],
        'scissors': ['rock']
    },
    'tie': {
        'rock': ['rock'],
        'paper': ['paper'],
        'scissors': ['scissors']
    }
}

# Define function to get user input
def get_user_input():
    # Ask user to select an option
    print("Select an option:")
    for key, value in options.items():
        print(f"{key}: {value}")
    user_input = int(input())
    # Validate user input
    while user_input not in options.keys():
        print("Invalid option. Please select a valid option:")
        for key, value in options.items():
            print(f"{key}: {value}")
        user_input = int(input())
    return options[user_input]

# Define function to get computer input
def get_computer_input():
    computer_choice = random.choice(list(options.values()))
    return computer_choice

# Define function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif computer_choice in rules[user_choice]:
        return 'win'
    else:
        return 'lose'

# Define function to display game results
def display_results(user_choice, computer_choice, result):
    if result == 'tie':
        print(f"It's a tie! You both chose {user_choice}.")
    elif result == 'win':
        print(f"You win! {user_choice} beats {computer_choice}.")
    else:
        print(f"You lose! {computer_choice} beats {user_choice}.")
    print()

# Define function to play the game
def play_game():
    # Get user input
    user_choice = get_user_input()
    # Get computer input
    computer_choice = get_computer_input()
    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    # Display the results
    display_results(user_choice, computer_choice, result)

# Define function to ask user if they want to play again
def play_again():
    play_again = input("Do you want to play again? (yes/no): ").lower()
    return play_again

# Define main function
def main():
    while True:
        play_game()
        play_again_input = play_again()
        if play_again_input == "no":
            print("Thanks for playing! Goodbye!")
            break

# Call main function
if __name__ == "__main__":
    main()
