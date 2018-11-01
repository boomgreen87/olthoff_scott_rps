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

	print("\n=================================================================\n")

	# Receive's  Player's choice and display it
	print("Choose your weapon!")
	player = input("'Rock', 'Paper', or 'Scissors'? (Type 'X' to exit)\n")

	# Quits game if Player types in "Quit"
	if player == "X" or player == "x":
		exit()

	#If there is a tie, neither player loses a life
	if (player == computer):
		print("\nTie! Get it together!\n")

	#If one player wins, the other player loses a life
	elif player == "Rock": # Player choice = Rock
		if computer == "Paper": # Computer choice = Paper, Computer won
			print("\nYou lose!", computer, "covers", player, "!\n")
			playerLives -= 1
		else: # Computer choice = Scissors, Computer lost
			print("\nYou win!", player, "smashes", computer, "!\n")
			compLives -= 1

	elif player == "Paper": # Player choice = Paper
		if computer == "Scissors": # Computer choice = Scissors, Computer won
			print("\nYou lose!", computer, "cuts", player, "!\n")
			playerLives -= 1
		else: # Computer choice = Rock, Computer lost
			print("\nYou win!", player, "covers", computer, "!\n")
			compLives -= 1

	elif player == "Scissors": # Player choice = Scissors
		if computer == "Rock": # Computer choice = Rock, Computer won
			print("\nYou lose!", computer, "smashes", player, "!\n")
			playerLives -= 1
		else: # Computer choice = Paper, Computer lost
			print("\nYou win!", player, "cuts", computer, "!\n")
			compLives -= 1

	# Asks user to re-enter choice if the input is not one of the options
	else:
		print("Not a valid option. Please re-enter your choice, and check your spelling!\n")

	# Prints the remaining lives of each player
	print("Player Lives:\t", playerLives, "/ 3")
	print("Computer Lives:\t", compLives, "/ 3")

	# Displays who won and asks the user if they would like to play again or quit then performs accordingly
	if playerLives == 0 or compLives == 0:
		if playerLives == 0:
			print("\n****************************\nComputer won the game!\n****************************\n")
		else:
			print("\n****************************\nYou won the game!\n****************************\n")

		while replay is False:
			replay = input("Would you like to play again? (Y/N)\n")

			if replay == "Y" or replay == "y":

				#Resets lives for new game and starts a new game
				playerLives = 3
				compLives = 3

			elif replay == "N" or replay == "n":
				#Quits the app
				exit()

			# Asks user to re-enter choice if the input is not one of the options
			else:
				print("\nNot a valid option. Please re-enter your choice.\n")
				replay = False

		# Resets replay value
		replay = False

	#Resets player value so loop continues
	player = False
