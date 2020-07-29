class Students:
    def __init__(self, id, name, grade_list):
        self.id = id
        self.name = name
        self.grade_list = grade_list

    def add_grade(self):
        grade_list[crs] = grade
        return grade_list

    def __str__(self):
        return f'{self.name}\nyour grade list: {grade_list}'


    def calc_factor(self):
        new_grade = grade_list[crs] * (fac / 100 + 1)
        if new_grade > 100:
            new_grade = 100
        return new_grade

    def average(self):
        sum1 = 0
        for i in grade_list:
            sum1 += grade_list[i]
        return sum1 / len(grade_list)




grade_list = {}
student1 = Students(319025599, "Roy", grade_list)

print(f'Hello {student1.name}!')
print("1 - add grade to course")
print("2 - calculate factor")
print("3 - calculate average grade")
print("4 - show your details")
print("0 - Exit")

option = int(input("Choose Option: "))
while option != 0:
    if option == 1:
        crs = input("Enter course name: ")
        grade = int(input("Enter grade: "))
        print(student1.add_grade())

    if option == 2:
        crs = input("Enter course name: ")
        fac = int(input("Enter factor: %"))
        print(student1.calc_factor())

    if option == 3:
        print(student1.average())

    if option == 4:
        print(student1)

    option = int(input("Choose Option: "))

