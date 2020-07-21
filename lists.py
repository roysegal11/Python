def targil1():
    from random import randint
    num1 = randint(1, 100)
    print(num1)


def targil2():
    list1 = list(range(1, 11))
    print(list1)

    list2 = []
    for i in range(1, 11):
        list2.append(i)
    print(list2)


def targil3():
    list1 = list(range(1, 11))
    print(list1[7:11])


def targil4():
    list1 = list(range(1, 11))
    print(list1[::-1])


def targil5():
    list1 = list(range(1, 11))
    print(list1[1::2])


def targil6():
    list1 = list(range(1, 11))
    print(list1[:5])


def targil7():
    list1 = list(range(1, 11))
    print(list1[::2])


def targil8():
    num1 = int(input("Number: "))
    list1 = list(range(1, 11))
    list1[7:10] = [num1]
    print(list1)

def targil13():
    from random import randint
    list1 = []
    for i in range(1,21):
        num1 = randint(1, 100)
        list1.append(num1)
    print(list1)

    num2 = int(input("Insert number: "))
    for long in (list1):
        if long == num2:
            list1.remove(num2)
    print(list1)


def targil17():
    list1 = (input("numbers: "))
    list2 = (input("numbers: "))
    list1New = list1.split(" ")
    list2New = list2.split(" ")
    print(list1New)
    print(list2New)
    for check1 in (list1New):
        if check1 in (list2New):
                print("Same Same New List")
                break


targil17()

# str1 = "roy segal"
# list1=[]
# for i in str1:
#     if i not in list1:
#         list1.append(i)
# print(list1)


