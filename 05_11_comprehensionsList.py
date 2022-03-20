# [expression for item in items]

items = [("Prod4", 3), ("Prod2", 1), ("Prod3",-2)]

# ~ map(lambda, iterable)
print([item[1] for item in items])

print([item for item in items if item[1]>0])
