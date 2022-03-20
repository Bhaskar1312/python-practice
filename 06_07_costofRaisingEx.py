from timeit import timeit

code1= """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cant be zero or less")
    return 10/age
try:
    calculate_xfactor(-1)
except ValueError as ex:
    print(ex)
"""
code2= """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cant be zero or less")
    return 10/age
try:
    calculate_xfactor(-1)
except ValueError as ex:
    pass
"""
code3= """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age
res = calculate_xfactor(-1)
if res == None:
    pass
"""
print(timeit(code1, number=10000))
print(timeit(code2, number=10000))
print(timeit(code3, number=10000))