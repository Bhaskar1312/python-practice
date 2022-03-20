class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

point = Point(1,-2)
print(point.__str__())
point2 = Point(1,-2)
print(point == point2)
point3 = Point(2,3)
print(point3 > point2)
print(point3 < point2)
print(point2 < point3)

print(point+point2)