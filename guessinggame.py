answer = 5

print("Please guess a number from 1 to 10: ")
guess = int(input())

if guess == answer:
    print("You got it first time.")
else:
    if guess < answer:
        print("Please guess higher.")
    else:
        print("Please guess lower.")
    guess = int(input())
    if guess == answer:
        print("You have got it!")
    else:
        print("Sorry, you missed it.")

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher.")
#     else:
#         print("Please guess lower.")
#     guess = int(input())
#     if guess == answer:
#         print("You have got it!")
#     else:
#         print("Sorry, you missed it.")
# else:
#     print("You got it first time.")


# if guess < answer:
#     print("Please guess higher.")
#     guess = int(input())
#     if guess == answer:
#         print("You made it!")
#     else:
#         print("You guessed incorrectly.")
# elif guess > answer:
#     print("Please guess lower.")
#     guess = int(input())
#     if guess == answer:
#         print("You made it!")
#     else:
#         print("You guessed incorrectly.")
# else:
#     print("You got it first time!")
