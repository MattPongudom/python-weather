# value = input("Please enter a value:\n")
#
# print(value)

import sys
import random
from enum import Enum


def rps(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0
    both_tie = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        nonlocal both_tie

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSOR = 3

            # print(RPS(2))
            # print(RPS.ROCK)
            # print(RPS['ROCK'])
            # print(RPS.ROCK.value)
            # sys.exit()

        playerchoice = input(f"\n{name}, please enter... \n1 for Rock, \n2 for Paper, \n3 for Scissor:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n{name}, please chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        def decide_winer(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            nonlocal both_tie
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name}, You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name}, You win!)"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name}, You win!)"
            elif player == computer:
                both_tie += 1
                return "🤝 You are both tied!"
            else:
                python_wins += 1
                return f"🐍 Python wins!\nSorry, {name}..."

        game_result = decide_winer(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame Count:{game_count}")
        print(f"\n{name}'s wins:{player_wins}")
        print(f"\nPython wins:{python_wins}")
        print(f"\nBoth tie:{both_tie}")

        print(f"\n Play again, {name}?")

        while True:
            playagain = input("\n Y for Yes \n Q for Quit\n ")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("🙏🙏Thank\'s for playing.\n")
            sys.exit(f"Bye {name}! 👋")

    return play_rps


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provide a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
