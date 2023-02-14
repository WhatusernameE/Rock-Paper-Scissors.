import random

print("Welcome to rock paper scissors.")

print("Do you want to play a game?")

user = input("Yes or No?")

player = False

if user == "Yes" or "yes":
    print("Ok before we begin you have a choice between best of 3,5 or 7")

    best = int(input("Best of (Number please.) "))

    print("You have chosen best of ", best, "\n")

    rock = 1

    paper = 2

    scissors = 3

    computer = random.randint(0, 3)

    rounds = 0

    while rounds < best:
        player = int(input("Rock, Paper or Scissors? (Rock: 1 Paper: 2 Scissors: 3)"))

        if player == computer:
            print("Tie!")

        elif player == 1:
            if computer == 2:
                print("You Lose!", computer, "Covers", player)
            else:
                print("You Win!", player, "Smashes", computer)
        elif player == 2:
            if computer == 3:
                print("You Lose!", computer, "Cuts", player)
            else:
                print("You Win!", player, "Covers", computer)
        elif player == 3:
            if computer == 1:
                print("You Lose!", computer, "Smashes", player)
            else:
                print("You Win!", player, "Cuts", computer)
        else:
            print("That's Invalid Check that you are inputting a number not the word.")
            quit()
        player = False
        computer = random.randint(0, 3)

        rounds = rounds + 1
        print("How many rounds you've done: ", rounds, '\n')
        if rounds == best:
            print("Since you chose best of ", best, "the game has ended.")
