
list1 = [1,2,3]
list2 = [10,20,30]
res = zip(list1, list2, range(100, 400, 100), "abc")
print(list(res))