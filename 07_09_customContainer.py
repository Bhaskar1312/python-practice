"""
len(tags)
tags["python"] ?

"""
class TagCloud:
    def __init__(self):
        self.__tags = {}
        # pass
    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1
    def __len__(self):
        return len(self.__tags)
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)
    def __setitem__(self, tag, item):
        self.__tags[tag.lower()] = item
    def __iter__(self):
        return iter(self.__tags)
    

cloud = TagCloud()
cloud.add("python")
cloud.add("Python")
cloud.add("programming")
cloud.add("python")
print("length",len(cloud))
print(cloud["Python"])
print("Programming", cloud.__getitem__("programming"))
# print(cloud.__tags)

cloud['java'] =10
# print(cloud.__tags)

for i in iter(cloud):
    print(i)

# private variables are prefixed with __ , but they are still accessible from outside

print(cloud.__dict__)

print(cloud._TagCloud__tags)