# Guided Project: GitHub Copilot with Python

## Creating Text Games

1. Excercise

Develop a console-based Rock Paper Scissors Lizard Spock game in Python.
  The game is known from the sitcom "Big bang theory".
  Use GitHub Copilot with following comment-prompt:

  ``` markdown
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
  # Ask user if they want to play again
  # If user selects 'yes', repeat the game
  # If user selects 'no', exit the game
  ```

2. Practice task

  Develop a console-based Rock Paper Scissors game in Python.
  Use your own GitHub Copilot comment-prompt. My prompt was:

  ``` markdown
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
  ```

## Create text based adventure game

``` markdown
Develop a Python list named “clues” containing 10 sentences.
Each sentence should hint at past events, varying from grand and intense to understated and enigmatic.
Ensure these clues are versatile enough to be applicable in any room setting and structured in the format "There is a...".

Construct a Python list named “sense_exp” with 12 sentences.
Each should describe a sensory experience (sight, sound, smell, touch, intuition) fitting for any room in a castle.
Frame these sentences using phrases like "You see," "You hear," etc., aiming to create a mysterious and immersive atmosphere in a text-based adventure game.

Create a Python class named "RandomItemSelector".
The class should be structured as follows:

Initialization method "init": The class initializes with a list argument representing a collection of items.
Set up two instance variables within the constructor: "items" to store the original list of items, and "used_items"
as an empty list to keep track of items that have been selected.

Add item method "add_item": This method takes an item as a parameter and adds it to the "items" list,
allowing for expanding the selection pool dynamically.

Pull random item method "pull_random_item": This method selects a random item from the "items" list that
hasn't been selected previously. Once an item is selected, add it to the "used_items" list. If all items in the "items" list have been used,
reset the "used_items" list to make all items available for selection again. Handle the scenario where there are no items to select by resetting the list.

Reset method "reset": Include a method that clears the "used_items" list, making all items in the "items" list available for selection again.

The class should efficiently handle item selection and tracking, and be versatile for different types of item lists.
```
``` markdown
Follow the given guidelines to define the “SenseClueGenerator” class.
This includes importing “RandomItemSelector”, ensuring singleton pattern with new method,
initializing clue and sense selectors, and defining a method “get_senseclue” to combine clues and sensory experiences.

Start by importing the "RandomItemSelector" class at the beginning of your code.

Define the "SenseClueGenerator" class. In this class, implement the following:
In the "__new__" method of "SenseClueGenerator", check if a class variable named "_instance" is None.
If "_instance" is None, create a new instance of "SenseClueGenerator" and assign it to "_instance".
Also, initialize two member variables: "clue_selector" and "sense_selector". 
For each, create a new instance of "RandomItemSelector". Pass the "clues" list to the constructor of 
"clue_selector" and the "sense_exp" list to the constructor of "sense_selector".

Ensure that the "__new__" method returns the "_instance" class variable.

Define a method named "get_senseclue" in the "SenseClueGenerator" class. This method should:
Call the "pull_random_item" method on both "clue_selector" and "sense_selector". 
Assign the results to variables "clue" and "sense", respectively.
Return a string that combines the values of "clue" and "sense" into a cohesive narrative or description.

Create an enumeration called encounter_outcome that has 'CONTINUE', and 'END' using Python's built-in `enum` module.

Create an Encounter class that inherits from ABC making it an abstract base class. 
The run_encounter method is decorated with @abstractmethod, which makes it an abstract method. 
This means that any subclass of Encounter must provide an implementation of run_encounter. 
The result of run_encounter needs to return an EncounterOutcome.

Create a ‘DefaultEncounter’ class that inherits from the `Encounter` base class. 
When it is initialized it will instantiate an instance of  SenseClueGenerator and pass it. 
In the “run_encounter implementation it will call pull_random_item from the instance of SenseCLueGenerator 
it created when it was initialized. It will take the output of the call to pull_random_item. 
It will print what is returned from pull_random_item. It will return EncounterOutcome.CONTINUE.

Create a Room class that has a name and an encounter. 
The encounter and room name are set when the class is initialized. 
The room class will have a name and a visit_room member function. 
When the visit_room member function is called, the run_encounter function of encounter will be 
called and the result will be returned.

Create a list of 6 room objects. Each room should have the name of an interesting room that would be in a castle. 
Use the default encounter for each room.
```

``` markdown
Create a Python class named "Castle". Use the following guidelines for its structure and functionality:

1. Initialization method "__init__":
- Initialize a member variable called "room_selector" as a new instance of "RandomItemSelector", 
passing a predefined list "rooms" to its constructor.

2. Select Door Method "select_door":
- Implement a method "select_door" that randomly chooses a number between 2 and 4 (inclusive) representing doors.
- Display the number of doors to the user.
- Prompt the user to select a door number.
- Validate the user's input. If it's not a valid number or out of the specified range, display an error 
message and prompt for input again. Repeat this process until a valid input is received.

3. Next Room Method "next_room":
- Create a method "next_room" that first calls "select_door".
- After a door is selected, use "pull_random_item" from the "room_selector" to obtain a random room.
- Display the name of the chosen room to the user.
- Call the "visit_room" method of the chosen room and return its result.

4. Reset Method "reset":
- Implement a method named "reset" which calls the reset method of the "room_selector".
Ensure that all printed outputs from these methods are well-formatted and easy to read for a better user experience.
```

``` markdown
Create a Python class named 'Game'. The class should be structured as follows:

1. Initialization method 'init':
-The class initializes with a parameter 'rooms', which is a set of room objects.
-Inside the 'init' method, create an instance of the 'Castle' class and pass the 'rooms' set to it.

2. Member function 'play_game':
-Implement the 'play_game' method. This method should first explain the game's objective to the user: 
to navigate through the castle and find the treasure.
-After explaining, start the game loop within this method.

3. Game loop in 'play_game':
-The loop should continuously call the 'next_room' member function of the 'Castle' instance.
-Check the return value of 'next_room'. If it returns 'EncounterOutcome.END', then:
–Call the 'reset' member function of the 'Castle' instance.
—Display a message 'Game Over' to the user.
-Ask the user if they would like to explore a different castle.
-If 'next_room' returns 'EncounterOutcome.CONTINUE', the loop should continue by calling 'next_room' again.

Ensure the 'Game' class efficiently manages the gameplay loop and user interactions
```

``` markdown
Create a game class. The game class takes a set of rooms in the init. 
The game creates a “Castle” instance when initialized and passes the set of rooms to it. 
The game class has a member function called “play_game.” When “play_game” is called it explains 
the game to the user which is to navigate the castle and find the treasure to win. 
Then it starts the game loop.

The game loop occurs as follows: 

-it calls the Castle “next_room” member function. 
-If “EncounterOutcome.END” is returned then it calls the reset member function of “Castle”, 
says “Game Over” and asks the player if they would like to explore a different castle. 
-If “EncoutnerOutcome.CONTINUE” then “Castle” “next_room” is called again.
```

``` markdown
# add a Treasure Room with a Treasure Encounter to the rooms list

Create a RedWizard encounter that inherits from the `Encounter` base class. 
In the “run_encounter” have the user play a game of rock paper scissors lizard spock with the wizard.
These are the game rules:

 - Scissors decapitate lizard
 - Scissors cuts paper
 - Paper covers rock 
 - Rock crushes lizard 
 - Lizard poisons Spock 
 - Spock smashes scissors 
 - Lizard eats paper 
 - Paper disproves Spock 
 - Spock vaporizes rock 
 - Rock crushes scissors

Use the following code for the game rules:
```
``` csharp
game_rules = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["rock", "scissors"]
}
```

``` markdown
If it is a draw, the game is played again, if the user wins the user is given the message that the 
red wizard has been vanquished from this castle and EncounterOutcome.CONTINUE is returned. 
If the wizard wins, tell the user they have been vanquished from this castle and EncounterOutcome.END. 
The printed output is well formatted and easy to read.

# create a room called “The Red Wizard’s Lair” with the Red Wizard Encounter and add it to the rooms list

Create alternatives to the Rock, Paper, Scissor, Spock, Lizard options of the game that better fit a wizard in a fantasy setting. 
Use the following game rules:
```
``` csharp
game_rules = {
    "Fireball": ["Ice Shard", "Lightning Bolt"],
    "Ice Shard": ["Wind Gust", "Earthquake"],
    "Wind Gust": ["Lightning Bolt", "Fireball"],
    "Lightning Bolt": ["Earthquake", "Ice Shard"],
    "Earthquake": ["Fireball", "Wind Gust"]
}
```
``` markdown
Change it from a game to a spell battle. If the wizard loses it is vanquished from this castle.
```








