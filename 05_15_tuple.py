point=1,2
point2=(1,3)
point3=3, # even () is tuple
print(type(point3))
print(point)
print(point2)
print(point+point2)

print(tuple([1,2]))
print(tuple("Hello World")[2:])

# unpacking
x, y, z, w = tuple("Hell")
print(x,y,z)

# swap, tuple
x, y = y, x
print(x,y)