def greet():
    print('Hello')

greet()


def greet(user):
    print(f'Hello {user}')

greet('Bhaskar')
greet('')


def my_round(x):
    return (int)(x+0.5)

print(my_round(3.4))
print(my_round(3.5))

# optional by param
def increment(number, by=1, another=3):
    return number+by

print("inc",increment(3, 2))
print(increment(4.3))
# keyword argument
print(increment(by=2, number=4.3))