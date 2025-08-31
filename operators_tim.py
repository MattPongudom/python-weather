a = 11
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)  # dividing floats
print(a // b)  # 4 integer division, round down towards minus infinity
print(a % b)  # only remainders

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print((((a + b) / 3) - 4) * 12)
print(((a + b) / 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print(a / (b * a) / b)
