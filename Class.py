class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def introduce(self):
        print('Em ten la',self.name,'.Em nam nay',self.age)

    def diem_trung_binh(self):
        s=sum(self.score.values())
        print('Diem trung binh cua',self.name,'la',s/len(self.score))

    def diem_trung_binh_lop(students):
        if not students:
            print('Loi')
        s = 0
        t=0
        for i in students:
            s=sum(i.score.values())
            a=s/len(i.score)
            t=t+a
        print('Diem trung binh cua lop la',t/len(students))

s1 = Student('An', 18, {'Toan': 9, 'Anh': 8, 'Van': 7})
s2 = Student("Binh", 17, {'Toan': 6, 'Anh': 7, 'Van': 8})
s3 = Student("Cuong", 16, {'Toan': 10, 'Anh': 9, 'Vam': 9})

students = [s1, s2, s3]

s1.introduce()
Student.diem_trung_binh(s1)
Student.diem_trung_binh_lop(students)
