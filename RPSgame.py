from random import randint

# Available weapons => Store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

# Sets initial lives for each player
compLives = 3;
playerLives = 3;

#Sets initial replay value
replay = False

#Loops the game until one player loses
while player is False:

	# Make the computer pick one item at random
	computer = choices[randint(0, 2)]

	# Receive's  Player's choice and display it
	print("Choose your weapon!")
	player = input("'Rock', 'Paper', or 'Scissors'? (Type 'Quit' to exit)\n")
	print("\nPlayer chooses:", player, "\n")

	# Show the computer's choice in the terminal window
	print("Computer chooses: ", computer, "\n")

	#If there is a tie, neither player loses a life
	if (player == computer):
		print("Tie! Get it together!\n")

	#If one player wins, the other player loses a life
	elif player == "Rock": # Player choice = Rock
		if computer == "Paper": # Computer choice = Paper, Computer won
			print("You lose!", computer, " covers ", player, "!\n")
			playerLives -= 1
		else: # Computer choice = Scissors, Computer lost
			print("You win!", player, " smashes ", computer, "!\n")
			compLives -= 1

	elif player == "Paper": # Player choice = Paper
		if computer == "Scissors": # Computer choice = Scissors, Computer won
			print("You lose!", computer, " cuts ", player, "!\n")
			playerLives -= 1
		else: # Computer choice = Rock, Computer lost
			print("You win!", player, " covers ", computer, "!\n")
			compLives -= 1

	elif player == "Scissors": # Player choice = Scissors
		if computer == "Rock": # Computer choice = Rock, Computer won
			print("You lose!", computer, " smashes ", player, "!\n")
			playerLives -= 1
		else: # Computer choice = Paper, Computer lost
			print("You win!", player, " cuts ", computer, "!\n")
			compLives -= 1

	# Quits game if Player types in "Quit"
	elif player == "Quit":
		exit()

	# Asks user to re-enter choice if the input is not one of the options
	else:
		print("Not a valid option. Please re-enter your choice, and check your spelling!\n")

	# Prints the remaining lives of each player
	print("Player Lives: ", playerLives)
	print("Computer Lives: ", compLives, "\n")

	# Displays who won and asks the user if they would like to play again or quit then performs accordingly
	# Computer wins game
	if playerLives == 0:
		print("Computer won the game!\n")

		while replay is False:
			replay = input("Type 'Play Again' to play another game or 'Quit' to exit.\n")

			if replay == "Play Again":
				print("\n\n")

				#Resets lives for new game and starts a new game
				playerLives = 3
				compLives = 3

			elif replay == "Quit":
				#Quits the app
				exit()

			# Asks user to re-enter choice if the input is not one of the options
			else:
				print("\nNot a valid option. Please re-enter your choice, and check your spelling!\n")
				replay = False

		# Resets replay value
		replay = False

	# Player wins game
	if compLives == 0:
		print("You won the game!\n")

		while replay is False:
			replay = input("Type 'Play Again' to play another game or 'Quit' to exit.\n")

			if replay == "Play Again":
				print("\n\n")

				#Resets lives for new game and starts a new game
				playerLives = 3
				compLives = 3

			elif replay == "Quit":
				#Quits the app
				exit()

			# Asks user to re-enter choice if the input is not one of the options
			else:
				print("\nNot a valid option. Please re-enter your choice, and check your spelling!\n")
				replay = False

		# Resets replay value
		replay = False

	#Resets player value so loop continues
	player = False
