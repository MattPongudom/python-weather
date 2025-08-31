#

name = "Dave"  # these are global scope
count = 1


def another():
    color = "blue"  # under local scope
    global count  # to add 1 to global scope --- previous 'count = 2' which has no connection to global scope
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Dave")


another()
