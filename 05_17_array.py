from array import array

# google typecode
# https://docs.python.org/3/library/array.html#:~:text=The%20following%20type%20codes%20are%20defined%3A%20%20,%20%20%20%209%20more%20rows%20
numbers = array("i", [0,1,2,3])
print(numbers)
numbers.pop()
numbers.remove(0)
numbers.append(4)
print(numbers)