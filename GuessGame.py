import random
import math
# Taking Inputs
lower_limit = int(input("Enter Lower bound:- "))

# Taking Inputs
# ab = int(input("Enter Upper bound while starting from zero:- "))
upper_limit = int(input("Enter Upper bound:- "))

# generating random number between
# the lower and upper
x = random.randint(lower_limit, upper_limit)

'''For generating a single random number we can use the below function
but it will choose a number in decimals which is too difficult
to choose, so using the function random.randit()
to set the upper and lower limits'''
# x = random.random()


# To define the number of chances the player is having
# Print("Want to play in Easy mood, Normal or Hard")
# a=int(input("Enter the number of chances you want to choose the number in"))
a=5
print("you have ", a, "Chances to guess the number" )
# To count the number of guesses.
# count = 0


# while count < math.log(upper - lower + 1, 2):
for count in range(a):
# while count<a:
	count += 1

	# taking guessing number as input
	guess = int(input("Guess a number:- "))

	# Condition testing
	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		# Once guessed, loop will break
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

# If Guessing is more than required guesses,
# shows this output.
# if count >= math.log(upper - lower + 1, 2):
if count>=a:
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")

# Better to use This source Code on pycharm!
