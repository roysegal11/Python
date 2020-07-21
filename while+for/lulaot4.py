def targil1():
    num = int(input("Enter number: "))
    low = 0
    while num != 0:
        if 0 < num and (num < low or low == 0):
            low = num
        num = int(input("Enter number: "))

    print(low)


def idos():
    num = -1
    while num < 0:
        num = int(input("Enter number: "))

    min = num
    while num != 0:
        if num < min and not num < 0:
            min = num
        num = int(input("Enter number: "))

    print(min)


def targil2():
    num = int(input("Enter number: "))
    while num > 9 or num < -9:
        if num < 0:
            num = num * -1
        num = num // 10

    print(num)


def targil3():
    global serial
    high = 0
    for i in range(1, 8):
        num = int(input("Enter number: "))
        if num > high:
            high = num
            serial = i
    print("The Serial of the highest number is:", serial)


def targil4():
    num = int(input("Enter number: "))
    while num != 0:
        single = num % 10
        num = num // 10
        print(single, end="")


targil4()
