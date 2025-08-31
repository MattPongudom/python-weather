def add_one(num):
    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)  # at this point, only 1-9 will be shown. --- without 'return' 10 will be replaced by 'None'


mynewtotal = add_one(0)  # This will show 1-10
print(mynewtotal)
