items = [("Prod4", 3), ("Prod2", 1), ("Prod3",-2)]

# transform, or map
prices =[]
for item in items:
    prices.append(item[1])

print(prices)

mapobject =map(lambda item:item[1], items)
print(list(mapobject))

# filter based on some param
filtered = filter(lambda item: item[1]>0, items)
print(list(filtered))