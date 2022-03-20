class Text(str):
    def duplicate(self):
        return self + self

text = Text("Python")
print(text.lower())
print(text.duplicate())

class TrackableList(list):
    def append(self, object) :
        print("append called")
        return super().append(object)


tl = TrackableList()
tl.append("1")

