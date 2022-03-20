
#  1 2 3 how? instead of [1, 2, 3]
arr = [1,2, 3]
print(arr)
print(*arr)
# in javascript spread operator ...arr same as unpack here

print(*range(5))

values = [*range(5), *arr, *"abcde", '?']
print(values)

# unpack dict
first = {'x':1, 'y':2}
second = {'x':3, 'z':2}
combined = {**first, **second}
print(combined)

sentence = "This is a common interview question"
mymap = {}
ans = '?'
for x in sentence:
    val = mymap.get(x, 0) + 1
    mymap.update({x : val})
    # print(x, val)
    if val >= mymap.get(ans,0):
        ans = x
print("This is ans>>", ans, "<< repeated ", mymap.get(ans), " times")
print(sorted(mymap, key=lambda kv: mymap[kv]))

from pprint import pprint
pprint(mymap, width=1)
pprint(sorted(mymap.items(), key=lambda kv:kv[1], reverse=True))