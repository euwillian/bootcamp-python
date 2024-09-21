import random
import rps_art_game

# The Basic Rules of RPS

# Despite its underlying complexity, the game’s rules are straightforward.
# Players deliver hand signals representing rock, paper, or scissors,
# with the outcome determined by these three rules:

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

print("*** Welcome to Rock, Paper or Scissors game ***")
print("What do you choose: Type 0 for Rock, 1 for Paper or 2 for Scissors!")
user_input = int(input(">>> "))
computer_input = random.randint(0, 2)

if user_input == 0 or user_input == 1 or user_input == 2:

    print("\nYOU:")

    if user_input == 0:
        rps_art_game.rock()
    elif user_input == 1:
        rps_art_game.paper()
    else:
        rps_art_game.scissors()

    print("COMPUTER:")

    if computer_input == 0:
        rps_art_game.rock()
    elif computer_input == 1:
        rps_art_game.paper()
    else:
        rps_art_game.scissors()

    # Game rules:

    if user_input == computer_input:  # rock vs rock or paper vs paper or scissors vs scissors = draw
        print("Draw")
    elif user_input == 0 and computer_input == 1:  # rock vs paper = paper
        print("You lose!")
    elif user_input == 0 and computer_input == 2:  # rock vs scissors = rock
        print("You win")
    elif user_input == 1 and computer_input == 0:  # paper vs rock = paper
        print("You win")
    elif user_input == 1 and computer_input == 2:  # paper vs scissors = scissors
        print("You lose")
    elif user_input == 2 and computer_input == 0:  # scissors vs rock = rock
        print("You lose")
    elif user_input == 2 and computer_input == 1:  # scissors vs paper = scissors
        print("You win")
    else:
        print("Error!")
else:
    print("Sorry! Invalid option, try again.")
