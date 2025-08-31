# Dictionaries - look alike javascript's 'objects'
from enum import member

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")  # output same as first set (line 3-6) - another way to set dict.

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items in dictionaries
print(band["vocals"])
print(band.get("guitar"))

print("")
# list all keys
print(band.keys())

print("")
# list all values
print(band.values())

print("")
# list of key/values pairs as tuples
print(band.items())

print("")

# verify if the key exists
print("guitar" in band)  # answer = true or false
print("triangle" in band)  # answer = true or false

print("")

# change values in dict.
band["vocals"] = "Coverdale"  # changed from "Plant" to "Coverdale"
band.update({"bass": "JPJ"})
print(band)

print("")

# remove items
print(band.pop("bass"))  # "bass" is removed from the dict.
print(band)

band["drums"] = "Bonham"
print(band)
print(band.popitem())
print(band)

print("")

# delete and clear items
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

print("")

# copy dictionaries
# band2 = band  # create a reference
# print("Bad copy!")
# print(band2)
# print(band)
#
# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band2)
print(band)

print("")

# copy by use dict() constructor function
band3 = dict(band)
print("Good copy!")
print(band3)

print("")

# nested dictionaries
member1 = {
    "name": "Plant",
    "instrument": "Vocals"
}
member2 = {
    "name": "Page",
    "instrument": "Guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])

print("")

# Sets
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))  # output same as above
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

print("")

# no duplicate allowed
nums = {1, 2, 2, 3}
print(nums)

# true is a dupe of 1, false is a dupe of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in set
print(2 in nums)

# but you cannot refer to an element in the set with an index position or a key

# add a new element to the set
nums.add(8)
print(nums)

# add element from one to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples, dictionaries, too.

# merge two sets to create a new set
one = {1, 2, 3}
two = {4, 5, 6}

mynewset = one.union(two)
print(mynewset)

# keep ony duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)  # show only duplicates numbers
print(one)

# keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
