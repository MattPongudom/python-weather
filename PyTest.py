import sys
from datetime import datetime


def show_date() -> None:
    print('This is the current date and time:')
    print(datetime.now())


show_date()


def greet(name: str) -> None:
    print(f'Hello, {name}!')


greet('Matt')
greet('Aim')

print(sys.version)
