class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self, fullname, age, is_married):
        print(f'Name:{fullname}\nAge:{age}\nSocial Status:{is_married}')


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        Person.__init__(self, fullname, age, is_married)
        self.marks = marks

    def find_marks(self):
        for k, v in self.marks:
            print(sum(v) / len(k))


def create_students():
    student1 = Student(fullname='Kanat', age=19, is_married='None', marks={
        'Eng': 10,
        'History': 7,
        'Math': 8,
        'IT': 9
    })
    student2 = Student(fullname='Alexa', age=29, is_married='Yes', marks={
        'Eng': 8,
        'History': 4,
        'Math': 10,
        'IT': 9
    })
    student3 = Student(fullname='Tim', age=23, is_married='None', marks={
        'Eng': 10,
        'History': 10,
        'Math': 10,
        'IT': 4
    })
    results = [student1, student2, student3]
    return results


students = create_students()
for i in students:
    list = []
    for marks in i.marks.values():
        list.append(marks)
    print(f"Name: {i.fullname}\n"
          f"Age: {i.age}\n"
          f"Maried: {i.is_married}\n"
          f"Average marks: {sum(list) / len(list)}\n")


class Teaher(Person):
    def __init__(self, fullname, age, is_married, experience=3):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = 10000

    def teacher_c(self):
        if self.experience >= 3:
            new_salary = self.salary + ((self.salary / 100 * 5)) * (self.experience - 3)
            return new_salary


st = Person('Kanat', 19, None)
print('Зарплата учителя')
teacher_info = Teaher('Azia', 46, 'Yes', 10)
print(f'{teacher_info.fullname} {teacher_info.age}, {teacher_info.is_married}')
print(teacher_info.teacher_c())
