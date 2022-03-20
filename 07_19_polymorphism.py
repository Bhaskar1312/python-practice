from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("Textbox")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")

def draw(control):
    control.draw()
def draw2(controls):  #controls - any object, duck typing
    for control in controls:
        control.draw()

ddl = DropDownList()
draw(ddl)
tb = TextBox()
draw(tb)

print("Testing")
draw2([ddl, tb])