age = int(input("Your age: "))

for i in range(2):
    while age > 0 and age <= 120:
        if 0 < age <= 18:
            print("Child")
            age = int(input("Your age: "))
        if 18 < age <= 60:
            print("Adult")
            age = int(input("Your age: "))
        if 60 < age <= 120:
            print("Senior")
            age = int(input("Your age: "))

    print("Invalid age")
    age = int(input("Your age: "))

print("Too many attempts")
# יש 3 נסיונות להציב נתון
