
class Car():
    tax = 1.1  #static attribute
    def __init__(self,brand,price):
        self.brand = brand   #public
        self.__price = price #public
car_1 = Car('Vinfast', 10000)
car_2 = Car('BMW',20000)
print(car_1._Car__price)
