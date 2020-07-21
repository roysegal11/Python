def small(a, b):
    if a < b:
        return a
    return b


def big(a, b):
    if a > b:
        return a
    return b


def two_num(a, b):
    for i in range(a, b + 1):
        print(i, end=" ")


num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))

num1, num2 = small(num1, num2), big(num1, num2)
two_num(num1, num2)
