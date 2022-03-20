class MyPoint:
    def draw(self):
        print('draw')

mp = MyPoint()
print(type(mp))
print(isinstance(mp, MyPoint))
print(isinstance(mp, int))
mp.draw()  