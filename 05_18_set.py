numbers = [1,2,2,4,5,6,6,6,10]
set2 = set([2, 9])
print(set(numbers))
set2.add(10)
set2.remove(2)
print(set2)

print(set(numbers) | set2)
print(set(numbers) & set2)
print(set(numbers) - set2)
print(set(numbers) ^ set2)