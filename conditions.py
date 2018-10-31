print("Rules that govern the state of water")

# Let the user pick a temp, see what happens to water (conditional statements)
# current_temp is the temperature variable (user inputs this)
current_temp = False

while current_temp is False:
	# User input - This changes temp on every iteration
	current_temp = input("Enter a temperature: \n")
	print(current_temp)

	# If it's 0 or lower, it is frozen
	if(int(current_temp) < 0) or (int(current_temp) == 0):
		print("Water is a solid. Icy AF!")
		current_temp = False

	# If it's between 0 and 100, it is liquid
	elif(int(current_temp) < 100):
		print("Water is a liquid. Too bad Flint still doesn't have any...")
		current_temp = False

	# If it's 100 or higher, it is a gas
	elif(int(current_temp) > 100) or (int(current_temp) == 100):
		print("Water is a vapor. Just blaze!")
		current_temp = False
