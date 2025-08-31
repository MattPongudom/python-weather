import math
import sys
import random
import kansas_dave
from rps7_dave import rock_paper_scissors
import random as rdm  # set alias
from enum import Enum

# from math import pi -- you have to use -- print(pi)

print(sys.version)
print("")
print(math.pi)
# sys.exit()
# exit()

random.choice("123")

for item in dir(random):
    print(item)

print(kansas_dave.capital)
kansas_dave.randomfunfact()
print(__name__)
print(kansas_dave.__name__)

rock_paper_scissors()
