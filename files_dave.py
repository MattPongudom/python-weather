import os
from gzip import WRITE
from pickle import APPEND
from winreg import CreateKey

from dotenv.parser import Reader


# r = Read
# a = APPEND
# w = WRITE
# x = Create
# Read - error if it doesn't exit

f = open("names")
# print(f.read())
# print(f.read(4)) # first 4 letters = Dave
# print(f.readline()) # first line appears = Dave
# print(f.readline()) # Jane appears with space line
# for line in f:
#     print(line)

f.close()

try:
    f = open("names") # the file name is right, the text will show.
    print(f.read())
except:
    print("The file doesn't exist.")
finally:
    f.close()

# Append - create the file that doesn't exist
f = open("names", "a")
f.write("Matt\n")
f.close()

f = open("names")
print(f.read())
f.close()

# Write - overwrite
f = open("context", "w")
f.write("I deleted all context.")
f.close()

f = open("context")
print(f.read())
f.close()

# two ways to create a new file
# open a file for writing, creates a file if doesn't exist

f = open("names_list", "w")
f.close()

# creates the specific file, but returns an error if the file exist.
if not os.path.exists("matt"):
    f = open("matt", "x")
    f.close()

# delete a file
# avoid an error if it doesn't exist
if os.path.exists("matt"):
    os.remove("matt")
else:
    print("The file to be deleted doesn't exist.")

with open("more_names") as f:
    content = f.read()
with open("names", "w") as f:
    f.write(content)
