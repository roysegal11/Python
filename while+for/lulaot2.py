def targil1():
    global avrg
    print("Enter number high then 100 to see the results")
    grade = int(input("Enter grade: "))
    high = 0
    sum = 0
    count = 0
    while 0 <= grade <= 100:
        count += 1
        sum = sum + grade
        if grade > high:
            high = grade
        avrg = sum / count
        print("The highest grade is:", high)
        print("The average grade is:", avrg)
        print("The differnce between the highest grade and the average is:", high - avrg)
        grade = int(input("Enter grade: "))
    print("The highest grade is:", high)
    print("The average grade is:", avrg)
    print("The differnce between the highest grade and the average is:", high - avrg)


def targil2():
    pass1 = input("Enter password: ")
    pass2 = input("Confirm password: ")
    count = 4
    while pass1 != pass2 and count > 0:
        count -= 1
        print("Invalid password")
        pass1 = input("Enter password: ")
        pass2 = input("valid password: ")
    if count == 0:
        print("Try again")
    else:
        print("Done!")


def targil3():
    num = int(input("Enter number: "))
    sum = 0
    while num != 0:
        sum += num % 10
        num = num // 10
    print(sum)
