class Product:
    def __init__(self, price):
        self.__set_price(price)
    def __get_price(self):
        return self.__price
    def __set_price(self, value):
        if value < 0:
            raise ValueError("Price can't be negative")
        self.__price = value
    price = property(__get_price, __set_price)

# product = Product(-10) # error
product = Product(10)
print(product.price)
# product.price = -10 # error

class Product2:
    def __init__(self, price):
        self.price = price
        # print(self)
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can't be negative")
        self.__price = value

# product2 = Product(-10) # error
product2 = Product2(10)
print(product2.price)
product2.price = -10 # error
# print(product2)

# if we comment out setter method, price is read-only
# comment 26-30 and check
