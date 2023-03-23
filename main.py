from art import logo
import random

print(logo)
# Welcome messages
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Get random number
number = random.randint(1, 100)
# Show random number just for testing
# print(f"Pssst, the correct answer is {number}")

attempts_remaining = 0
game_on = True

game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Check the level and assign attempts

if game_level == "easy":
	attempts_remaining += 10
elif game_level == "hard":
	attempts_remaining += 5
else:
	print("Invalid Level")

print(game_level)


# Check whether number is high or low
def checkNumber():
	global game_on
	global attempts_remaining
	print(f"attempts remaining: {attempts_remaining}")
	while game_on:
		if attempts_remaining > 0:
			user_guess = int(input("Make a guess: "))
			if user_guess > number:
				print("Too High")
				attempts_remaining -= 1
				print(f"You have {attempts_remaining} remaining to guess the number")
			elif user_guess < number:
				print("Too low")
				attempts_remaining -= 1
				print(f"You have {attempts_remaining} remaining to guess the number")
			else:
				print("You got it🔥😀")
				game_on = False
		else:
			game_on = False
			print("Game Over. You have run out of attempts")
			print(f"The number was {number}")


checkNumber()

# print()
