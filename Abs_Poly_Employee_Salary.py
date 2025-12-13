from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def calculate_annual_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self,name,monthly_salary):
        super().__init__(name)
        self.monthly_salary=monthly_salary
    def calculate_annual_salary(self):
        return f'Anual salary of {self.name}: {self.monthly_salary*12}'

class Contractor(Employee):
    def __init__(self,name,hourly_rate,hours_worked):
        super().__init__(name)
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked
    def calculate_annual_salary(self):
        return f'Anual salary of {self.name}: {self.hours_worked*self.hourly_rate}'

e=[FullTimeEmployee('Alex',12),Contractor('Brianna',1,6),Contractor('Channing',1.5,9),FullTimeEmployee('Dick',29)]
for i in e:
    print(i.calculate_annual_salary())
    