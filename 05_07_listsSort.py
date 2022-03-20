numbers = ['1', '2', '4', '2', '9', '8', '7']
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

arr = [1,3,5,7,2,3,4,-1]
print(sorted(arr)) # any iterables, will not change, but return sorted iteration
print(sorted(arr, reverse=True))
print(arr)

items = [("Prod4", 3), ("Prod2", 1), ("Prod3",-2)]
items.sort()
print(items)

def sort_by_second(item):
    return item[1]
items.sort(key=sort_by_second)
print(items)

# lambda
items.sort(key=lambda item:item[0])
print("lambda", items)

