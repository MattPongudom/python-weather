#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25::-1]
print(backwards)

backwards = letters[::-1]
print(backwards)

backwards = letters[16:13:-1]  # qpo
print(backwards)

backwards = letters[4::-1]  # edcba
print(backwards)

backwards = letters[25:17:-1]  # zyxwvuts
print(backwards)

backwards = letters[:-9:-1]  # zyxwvuts
print(backwards)

print(letters[-4:])  # wxyz
print(letters[-1:])  # z
print(letters[:1])  # a

print("Learn Python to be great!")

print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:-9:-1])

print(letters[-4:])
print(letters[-1:])

print(letters[1:])
print(letters[:1])
