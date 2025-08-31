# for i in range(1, 13):
#    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
# print("*" * 80)

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

# if age >= 18:
#    print("You are old enough to vote, nice!")
#    print("Please put an X on the form!")
# else:
#    print("Please come back in {0} year(s).".format(18 - age))

# two ways of diff conditions of blocks

if age < 18:
    print("Please come back in {0} year(s).".format(18 - age))
elif age == 900:
    print("You are already dead!")
else:
    print("You are old enough to vote, nice!")
    print("Please put an X on the form!")
