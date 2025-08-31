# value = input("Please enter a value:\n")
#
# print(value)

import sys
import random
from enum import Enum


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSOR = 3

    # print(RPS(2))
    # print(RPS.ROCK)
    # print(RPS['ROCK'])
    # print(RPS.ROCK.value)
    # sys.exit()

    playerchoice = input("\nEnter... \n1 for Rock, \n2 for Paper, \n3 for Scissor:\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', "") + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', "") + ".\n")

    if player == 1 and computer == 3:
        print("🎉 You win!)")
    elif player == 2 and computer == 1:
        print("🎉 You win!)")
    elif player == 3 and computer == 2:
        print("🎉 You win!)")
    elif player == computer:
        print("🤝 You are both tied!")
    else:
        print("🐍 Python wins!")

    print("\n Play again?")

    while True:
        playagain = input("\n Y for Yes\n Q for Quit\n ")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("🙏🙏Thank\'s for playing.\n")
        sys.exit("Bye! 👋")


play_rps()
