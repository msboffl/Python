#  Map() is a python in-built funtion that works an iterator  to return
#  a result after applying a function to every item of an iterable (tuple, lists, etc.).
#  It is used when you want to apply a single transformation function to all the iterable elements.

# Syntax : map(funtion(), Iterables)

numbers = [3, 5, 7, 11, 3]


def multiply(i):
    return i * i


X = map(multiply, numbers)
print(X)  # It prints a Address
print(list(X))  # It prints like array
