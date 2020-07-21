grade = int(input("Input grade: "))
sum = 0
count = 0
while grade >= 0 and grade <= 100:
    if grade >= 60:
        sum = sum + grade
        count += 1
    grade = int(input("Input grade: "))
print(count)
print (sum)