class Person():
    def __init__(self,name):
        self.name=name
    def greet(self):
        return f'Hello, I am {self.name}.'
class Student(Person):
    def __init__(self,name):
        super().__init__(name)
    def greet(self):
        return f'Hello, I am {self.name}. I am a student.'
class Teacher(Person):
    def __init__(self,name):
        super().__init__(name)
    def greet(self):
        return f'Hello, I am {self.name}. I am a teacher.'
s1=Student("Huynh Van B")
t1=Teacher('Le Thi C')
print(s1.greet())
print(t1.greet())