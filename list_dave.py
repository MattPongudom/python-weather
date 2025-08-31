# List

users = ['Dave', 'Mary', 'John']

data = ['Matt', 42, True]

emptylist = []

print("Dave" in users)
print("Dave" in emptylist)
print(users[0])
print(users[-1])
print(users[-2])
print(users.index('Mary'))
print(users[0:2])
print(users[0:])
print(users[1:])
print(users[-3:-1])
print(len(users))

users.append('Elsa')
print(users)
users += ['Billy']
print(users)

users.extend(['Bob', 'Ron'])
print(users)

# users.extend(data)  # not what we want
# print(users)

users.insert(0, 'Amy')
print(users)

users[2:2] = ['Francis', 'Gloria']  # not replacing the existing values
print(users)

users[1:3] = ['Jim', 'Ryan']  # replacing existing values
print(users)

users.remove('Mary')
print(users)

print(users.pop())  # pick up the last item of the list
print(users)  # all in the list except the last item

del users[0]  # delete the first (0) item of the list
print(users)

# del data - cannot do like this
data.clear()
print(data)

print("")

users[1:2] = ['henry']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

print("")

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)
print(sorted(nums, reverse=True))  # same output as above two lines
print(nums)  # output same as the reverse line 63-65
print("")
numscopy = nums.copy()  # all 72-74 are how to copy the original
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)
print(type(nums))
mylist = ([1, "Matt", True])
print(mylist)

print("")

# Tuples        # cannot be changed compared with lists
mytuple = tuple(('Matt', 52, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Glenn')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)
print("")
print(anothertuple.count(2))
