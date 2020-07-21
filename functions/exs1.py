num1 = int(input("3 Digits Number: "))


def sum1(a):
    sumi = a % 10 + a // 10 % 10 + a // 100
    return sumi


print(sum1(num1))
