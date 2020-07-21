def two_num(a, b):
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        print(i, end=" ")


# num1 = int(input("Enter number: "))
# num2 = int(input("Enter number: "))
#
#
# two_num(num1, num2)


def death(n, m):
    n = 10
    m = 10


a = 2
b = 3

print("A= " + str(a))
print("B= " + str(b))
death(a, b)
print("A= " + str(a))
print("B= " + str(b))
