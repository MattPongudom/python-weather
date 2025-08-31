class JustNotCoolError(Exception):
    pass


x = 2
try:
    raise JustNotCoolError("This is just not cool, man!")
    # raise Exception("I'm a custom exception!")
    # print(x / 0)
    # if not type(x) in str:
    #     raise TypeError("Only strings are allowed.")
except NameError:
    print('NameError means somthing is probably undefined')
except ZeroDivisionError:
    print('Please do not divide by zero.')

except Exception as error:
    print(error)
else:
    print('Mo errors!')
finally:
    print("I'm going to print without an error.")
