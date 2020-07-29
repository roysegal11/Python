class Students1:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        self.grades = {}

    def add_grade(self, name, grade):
        self.grades[name] = grade

    def __str__(self):
        return f'Hello {self.name}!\n{self.ID}'

    def calc_factor(self, subject, factor):
        new_grade = self.grades[subject] * (factor/100+1)
        if new_grade > 100:
            new_grade = 100
        self.grades[subject] = new_grade

    def average(self):
        sum1 = 0
        for i in self.grades:
            sum1 += self.grades[i]
        return sum1 / len(self.grades)


Roy = Students1(319025599, "Roy")
Gilad = Students1(318904802, "Gilad")



