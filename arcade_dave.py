import sys
from rps8_dave import rps
from guess_number_dave import guess_number


def play_game(name='PlayerOne'):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu.")

            playerchoice = input(
                "\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press \"x\" to exit the arcade.\n\n"
            )
            if playerchoice not in ["1", "2", "x"]:
                print(f"\n{name}, please enter 1, 2, or x.")
                return play_game()

            welcome_back = True

            if playerchoice == "1":
                rock_paper_scissors = rps(name)
                rock_paper_scissors()
            elif playerchoice == "2":
                guess_number = guess_number(name)
                guess_number()
            else:
                print("\nSee you next time1\n")
                sys.exit(f"Bye {name}!")


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
    print(f"\n{args.name}, welcome to the arcade!")

    play_game(args.name)
