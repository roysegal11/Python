from School.Students1 import Students1
from School.Course import Course


Shlomi = Course.add_student(name="Shlomi", ID=319925687)
print(Shlomi)


Roy = Students1(319025599, "Roy")
Gilad = Students1(318904802, "Gilad")
Roy.add_grade(name="QA", grade=90)
Roy.add_grade(name="Python", grade=95)
Gilad.add_grade(name="QA", grade=80)
Gilad.add_grade(name="Python", grade=85)
print(Roy)
print(Roy.grades)
print(Gilad)
print(Gilad.grades)

