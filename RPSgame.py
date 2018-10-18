from random import randint

# Available weapons => Store this in an array
choices = ["Rock", "Paper", "Scissors"]

# Make the computer pick one item at random
computerChoice = choices[randint(0, 2)]

# Show the computer's choice in the terminal window
print("Computer chooses: ", computerChoice)