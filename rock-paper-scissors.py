from random import randint


player = input("player, make your move: ").lower()

rand_num = randint(0,2)

if rand_num == 0:

	computer = "r"

elif rand_num == 1:

	computer = "p"

else:

	computer = "s"


print(f"Computer plays {computer}" )


if player == computer:

	print("It's a tie!")

elif player == "r":

	if computer == "s":

		print("player wins!")

	else:

		print("computer wins!")

elif player == "p":

	if computer == "r":

		print("player wins!")

	else:

		print("computer wins!")

elif player == "s":

	if computer == "p":

		print("player wins!")

	else:

		print("computer wins!")
else:

		print("please enter a valid move!")