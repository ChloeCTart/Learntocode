
class Car():
    tax = 1.1  #static attribute
    def __init__(self,brand,price):
        self.brand = brand   #public
        self._price = price #public
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        self._price=value
    
    @price.deleter
    def price(self):
        del self._price
car_1 = Car('Vinfast', 10000)
car_2 = Car('BMW',20000)
print(car_1._price)
car_1.price=30000
print(car_1.price)
del car_2.price
print(car_2.price)