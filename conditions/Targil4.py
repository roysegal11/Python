num1 = float(input("Enter number: "))
num2 = float(input("Enter number: "))

if num1 >= num2:
    num3 = num1-num2
else:
    if num2 >= num1:
        num3 = num2-num1
    else:
        print("No solution")

print(num3)

if num3 < 0:
    print(num3 * (-1))
else:
    print(num3)