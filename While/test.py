grade = int(input("Enter grade: "))

while grade > 100 or grade < 0:
    print("--")
    grade = int(input("Invalid grade!\nEnter new grade: "))

print(grade)

    # if grade >= 90:
    #     print("Very good")
    #
    # elif grade < 90 and grade >= 80:
    #     print("Good")
    #
    # elif grade < 80 and grade >= 70:
    #     print("O.K")
    #
    # elif grade < 70:
    #     print("Failed")