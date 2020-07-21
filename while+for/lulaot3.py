def targil1():
    sum = 0
    sum_old = 0
    for i in range(5):
        factor = int(input("Enter factor: "))
        grade = int(input("Enter grade: "))
        sum_old = sum_old + grade
        new_grade = grade * (factor / 100) + grade
        sum = sum + new_grade
        print(new_grade)
        print(sum)
    print(sum / 5)
    print(sum_old / 5)
    print(sum / 5 - sum_old / 5)


targil1()
