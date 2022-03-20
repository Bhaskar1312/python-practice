i =1
j =1
print(i==j)
print(id(i))
print(id(j))

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
p1 = Point(1, 2)
p2 = Point(1, 2)
print(id(p1))
print(id(p2))

print('named tuple')
from collections import namedtuple
Point2 = namedtuple("Point2", ["x", "y"])
p21 = Point2(x=1, y=1)
p22 = Point2(x=1, y=1)
print(id(p21))
print(id(p22))
print("p21 x", p21.x)
print(p21==p22)

# p21.x =10 #AttributeError: can't set attribute