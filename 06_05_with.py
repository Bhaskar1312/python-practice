from os import error


try:
    file = open('a.txt')
    print(file)
except FileNotFoundError as ex:
    print("No such file", ex)
finally:
    file.close()

try:
    with open("a.txt") as file, open('b.txt') as file2:
        # file.__enter__
        # file.__exit__
        # with ->closes automatically that have enter, exit methods
        print("File opened")
except error as ex:
    print(ex)
