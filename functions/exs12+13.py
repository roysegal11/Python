from random import randint

list1 = []


def RandList(a):
    for i in range(20):
        a.append(randint(1, 100))
    return list1


def FromList(a):
    if a in list1:
        return list1.count(a)


def MaxNum(a):
    return max(a)


print(RandList(list1))


num1 = int(input("Enter Number: "))
print("The number", num1, "showing up", FromList(num1), "times.")


print(MaxNum(list1))
