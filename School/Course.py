from School.Students1 import Students1

class Course:

    def __init__(self, course_num, course_name, subjects_list, students, full):
        self.course_num = course_num
        self.course_name = course_name
        self.subjects_list = subjects_list
        self.students = students
        self.full = full


    def add_student(self, name, ID):
        return Students1(ID, name)

    def __str__(self):
        return f'Hello {namenjo}'




