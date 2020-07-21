num1 = int(input("Number: "))


def f_sum(a):
    for i in range(1,a):
        a += i
    return a


print(f_sum(num1))

