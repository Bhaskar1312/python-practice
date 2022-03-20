# point = {"x":1, "y":2 }
point = dict(x=1, y=2)
print(point)
print(point['x'])
point['x']=10
print(point['x'])

if 'z' in point:
    print(point['z'])
else:
    print('Not found')
print(point.get("a"))
print(point.get("a", -1)) #default

del point['x']
point['a'] = 'a2'
print(point)

for key in point:
    print(key)

for x in point.items():
    print(x)

# dict comprehension
# [ expr for item in items]

print(list(zip("abcde", range(5))))
[ print(i,j) for i,j in zip("abcde", range(0,5)) ]
[ point.update({i: j}) for i,j in zip("abcde", range(0,5)) ]
print(point)

myset = { 2*x for x in range(5) }
print(myset)
mydict = {x : 2*x for x in range(5) }
print(mydict)