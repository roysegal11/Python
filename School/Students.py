class Students:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.grade_list = {}

    def add_grade(self,crs,grade):
        return self.grade_list.update({crs:grade})


    def __str__(self):
        return f'{self.name}\nyour grade list: {self.grade_list}'

    def calc_factor(self,crs,fac):
        new_grade = self.grade_list[crs] * (fac / 100 + 1)
        if new_grade > 100:
            new_grade = 100
        return new_grade

    def average(self):
        sum1 = 0
        for i in self.grade_list:
            sum1 += self.grade_list[i]
        return sum1 / len(self.grade_list)





Roy = Students(319025599, "Roy")
Gilad = Students(318904802, "Gilad")

# crs = "QA"
# grade = 90
# Roy.add_grade(crs,grade)
# crs = "Python"
# grade = 95
# Roy.add_grade(crs,grade)


#
# crs = "QA"
# grade = 80
# Gilad.add_grade(crs,grade)
# crs = "Python"
# grade = 85
# Gilad.add_grade(crs,grade)
#
# print(Roy)
# print(Gilad)







y_name = input("Enter Yor Name: ")
if y_name == "Roy":
    print(f'Hello {Roy.name}!')
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
            print(Roy.add_grade(crs,grade))

        if option == 2:
            crs = input("Enter course name: ")
            fac = int(input("Enter factor: %"))
            print(Roy.calc_factor(crs,fac))

        if option == 3:
            print(Roy.average())

        if option == 4:
            print(Roy)

    option = int(input("Choose Option: "))

if y_name == "Gilad":
    print(f'Hello {Gilad.name}!')
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
            print(Gilad.add_grade())

        if option == 2:
            crs = input("Enter course name: ")
            fac = int(input("Enter factor: %"))
            print(Gilad.calc_factor())

        if option == 3:
            print(Gilad.average())

        if option == 4:
            print(Gilad)

    option = int(input("Choose Option: "))
