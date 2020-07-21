grade = int(input("Enter Grade: "))

if grade >= 0 and grade <= 100: #if 0 <= grade <= 100:
    if grade >= 90:
        print("Very Good")
    else:
        if grade >= 80:
            print("Good")
        else:
            if grade >= 70:
                print("O.K")
            else:
               print("Failed")
else:
    print("Invalid grade")


if grade >= 0 and grade <= 100:
    if grade >= 90:
        print("Very Good")
    if grade < 90 and grade >= 80:
        print("Good")
    if grade < 80 and grade >= 70:
        print("O.K")
    if grade < 70:
        print("Failed")
else:
    print("Invalid Grade")


if grade >= 0 and grade <= 100:

    if grade >= 90:
        print("Very good")

    elif grade < 90 and grade >= 80:
        print("Good")

    elif grade < 80 and grade >= 70:
        print("O.K")

    elif grade < 70:
        print("Failed")

else:
    print("Invalid Grade")
