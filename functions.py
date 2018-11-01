# Let's explore some functions and how to write them and also what they do


def greeting():
	# Say hello
	print("Hello from your first function!")
	

# This is how you call or invoke a function
greeting()


# Function with multiple arguments
def greetings(msg="Hello there", num=0):
	print("Our function says: ", msg, "and the second arg is: ", num)

# Default argument
greetings()

# Custom arguments
greetings("This is an argument", 1)
greetings("Why are we arguing?", 2)

# In global scope
myVariableNumber = 0


def someMath(num1=2, num2=5):
	# Need to bring global scope variables into function's scope in order to use them
	global myVariableNumber

	myVariableNumber = num1 + num2
	return num1 + num2


sum = someMath()
print("Our sum variable is:", sum)