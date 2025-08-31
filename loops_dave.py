# 'while' loop
value = 1

# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
else:
    print("Value is now equal to " + str(value) + ".")

# 'for' loops
names = ["Dave", "Sara", "John"]
# for x in names:
#     print(x)
#
# for x in "Mississippi":
#     print(x)
for x in names:  # until finds "Sara" then stop but excluding "Sara"
    if x == "Sara":
        break
    print(x)

# for x in names:  # all except "Sara"
#     if x == "Sara":
#         continue
#     print(x)
#
# for x in range(4):  # start from '0'
#     print(x)

# for x in range(2, 4):  # start at '2' and stop at '4' -- you will get only 2 and 4
#     print(x)

# for x in range(0, 100, 5):  # start at '0' and stop at '100' -- increment by 5 (exclude 100)
#     print(x)
#
# for x in range(5, 101, 5):  # start at '5' and stop at '101' -- increment by 5 (exclude 101) top at 100
#     print(x)
# else:
#     print("Glad that\'s over!")

names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")
