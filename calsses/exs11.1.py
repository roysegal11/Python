class Course:
    def __init__(self, num, name, stud_num, stud_max):
        self.num = num
        self.name = name
        self.stud_num = stud_num
        self.stud_max = stud_max

    def describe(self):
        return f'course num is {self.num} its name is {self.name} there are {self.stud_num} students and the max students is {self.stud_max}'

    def available(self):
        return self.stud_max - self.stud_num


num = int(input("Class number: "))
name = input("Class name: ")
stud_num = int(input("Number of students: "))
stud_max = int(input("Max student: "))

a = Course(num, name, stud_num, stud_max)
print(a.describe())
print(a.available())
