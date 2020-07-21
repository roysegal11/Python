age = float(input("Enter your age here: "))

if 0 < age <= 120:
    if 0 < age <= 18:
        print("Child")
    elif 19 <= age <= 60:
        print("Adult")
    elif 61 <= age <= 120:
        print("Senior")
else:
    print("Invalid age")