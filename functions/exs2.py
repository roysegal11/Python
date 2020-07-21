def check_num(a):
    if 100 <= a <= 999:
        print("Pass")
    else:
        print("Try Again")
    return a


num1 = int(input("3 Digits Number: "))
while num1 != 0:
    check_num(num1)
    num1 = int(input("3 Digits Number: "))
