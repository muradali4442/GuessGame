import random

# Taking Inputs from the player
lower_limit = int(input("Enter Lower bound:- "))

upper_limit = int(input("Enter Upper bound:- "))

# To check if the choosen range is too small
if upper_limit-lower_limit<5:
	print("It's super easy, Choose the values with the difference more than 5")
	quit()

# Defining a function to guess the number
def guessGame(lower_limit, upper_limit):
	# generating random number between
	# the lower and upper limits
	x = random.randint(lower_limit, upper_limit)
	# To define the number of chances the player is having
	# To count the number of guesses.
	# count = 0
	y=5
	print("you have ", y, "Chances to guess the number")
	for count in range(y):
		count += 1

		# taking guessing number as input
		guess = int(input("Guess a number = "))

		# Condition testing
		if x == guess:
			print("You have choosen the right number in ",
				  count, " attempts")
			# To break the loop when the number choosen is correct
			break
			return x
		elif x > guess:
			print("Your guess is smaller than the exact number\n")
		elif x < guess:
			print("Your guess is higher than the exact number\n")

	# When the player fails to guess the right number,
	if count >= y:
		print("\nThe number is %d" % x)
		return x

# calling the function and passing the values to it
res=guessGame(lower_limit, upper_limit)

