from random import randint

# Available weapons => Store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

# Make the computer pick one item at random
computer = choices[randint(0, 2)]

# Show the computer's choice in the terminal window
print("Computer chooses: ", computer)


while player is False:
	print("Choose your weapon!")
	player = input("Rock, Paper, or Scissors?\n")
	print("Player chooses:", player)

	if (player == computer):
		print("Tie! Get it together!")

	elif player == "Rock":
		if computer == "Paper":
			# Computer won
			print("You lose!", computer, " covers ", player)
		else:
			print("You win!", player, " smashes ", computer)

	elif player == "Paper":
		if computer == "Scissors":
			# Computer won
			print("You lose!", computer, " cuts ", player)
		else:
			print("You win!", player, " covers ", computer)

	elif player == "Scissors":
		if computer == "Rock":
			# Computer won
			print("You lose!", computer, " smashes ", player)
		else:
			print("You win!", player, " cuts ", computer)

	elif player == "Quit":
		exit()

	else:
		print("Not a valid option. Please re-enter your choice, and check your spelling!\n")

	player = False
	computer = choices[randint(0,2)]
