values = (x for x in range(5))
print(values) # <generator object <genexpr> at 0x000001AB1D469510>

# memory efficient, generator obj dont store all values, they will give when asked

values2 = (x for x in range(5000000))
values3 = [x for x in range(5000000)]
from sys import getsizeof
print("gen", getsizeof(values)) #112
print("gen", getsizeof(values2)) #112
print("list", getsizeof(values3)) #43947864
# print(len(values2)) #no len for generator obj
print(len(values3))