class Student():
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
    @property
    def gpa(self):
        return self.__gpa
    @gpa.setter
    def gpa(self,value):
        if value>=0 and value<=4:
            self.__gpa=value
        else:
            raise ValueError("GPA must be between 0.0 and 4.0")
    def display(self):
        print(f'Student: {self.name}, GPA: {self.__gpa}')
s1=Student('Nguyen Van A',3.6)
print(s1.gpa)
s1.gpa=4.0
print(s1.gpa)
s1.display()
