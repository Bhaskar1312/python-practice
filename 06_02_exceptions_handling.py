# python 06_01_exceptions.py
try:
    age = int(input("Age: "))
    xfactor = 10/age
    if age <18 or age >60:
        raise SyntaxError
except (ZeroDivisionError, SyntaxError):
    print("Not a valid value ")
except ZeroDivisionError:
    print("Division by zero is undefined")
except ValueError as ex:
    print("You didn't enter numeric value")
    print(ex, type(ex))
else:
    print("No exception thrown")
print("Finished")