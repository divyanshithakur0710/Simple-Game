import random

def play_game():
    print("\nStone Paper Scissors Game")

    options = ["stone", "paper", "scissors"]

    user = input("Enter stone, paper or scissors: ")

    if user not in options:
        print("Invalid input")
        return

    computer = random.choice(options)

    print("Computer chose:", computer)

    if user == computer:
        print("Tie")
    elif user == "stone" and computer == "scissors":
        print("You win")
    elif user == "paper" and computer == "stone":
        print("You win")
    elif user == "scissors" and computer == "paper":
        print("You win")
    else:
        print("Computer wins")