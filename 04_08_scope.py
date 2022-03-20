message = 'a'

def greet():
    message = 'b' #different from global var above

def greet2():
    global message # global vars
    message = 'c'

greet()
print(message)
greet2()
print(message)