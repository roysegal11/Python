def Pass(a):
    if 0 <= a <= 100:
        return 70 <= a
    else:
        return None


for i in range(6):
    grade = int(input("Enter grade: "))
    if Pass(grade) is True:
        print("Passed")
    if Pass(grade) is False:
        print("Fail")
    if Pass(grade) is None:
        print("Not valid grade")




