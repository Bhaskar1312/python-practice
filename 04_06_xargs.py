def multiply(*numbers):
    print(numbers)
    print(type(numbers)) # tuple
    product = 1
    for x in numbers:
        product *= x
    print(product)
    return product

multiply(2,3,4,5)