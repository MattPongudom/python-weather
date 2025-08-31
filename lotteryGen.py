import random

# Option 1: Allow repeats (numbers can duplicate)
print("Thai Lottery Luck Numbers on Sept 1, 2025")
print("**********")

print("1st Prize")
random_numbers = [random.randint(0, 9) for _ in range(6)]
print(random_numbers)
print("")
print("Front 3 Digits")
random_numbers = [random.randint(0, 9) for _ in range(3)]
print(random_numbers)

random_numbers = [random.randint(0, 9) for _ in range(3)]
print(random_numbers)
print("")
print("Back 3 Digits")
random_numbers = [random.randint(0, 9) for _ in range(3)]
print(random_numbers)

random_numbers = [random.randint(0, 9) for _ in range(3)]
print(random_numbers)
print("")
print("2 Digits")
random_numbers = [random.randint(0, 9) for _ in range(2)]
print(random_numbers)
