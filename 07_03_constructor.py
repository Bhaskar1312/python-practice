class MyPoint:
    default_color = "red"
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self): #instance method
        print('draw', self.x, self.y)
    @classmethod
    def zero(cls): #class method, cls=convention
        return cls(0, 0)

mp = MyPoint(1,2)
print('x', mp.x)
mp.draw()

# class attribute shared across class
print(MyPoint.default_color)
print(mp.default_color)
MyPoint.default_color = "yellow"
print(MyPoint.default_color)
print(mp.default_color)

pt =MyPoint.zero() #factory method/class method
pt.draw()