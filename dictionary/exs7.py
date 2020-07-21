def targil1():
    dic1 = {1:10,2:20}
    dic2 = {3:30,4:40}
    dic3 = {5:50,6:60}
    dic1.update(dic2)
    dic1.update(dic3)
    print(dic1)
    print(dic1.keys())

    num1 = int((input("Key: ")))
    print(num1 in dic1.keys())


def targil2():
    dic1 = {1: 10, 2: 20, 3: 30, "a": 55}
    num1 = input("Here: ")
    print(dic1.keys())
    if type(num1) is str:
        if num1 in dic1:
            print("Yes")
    elif num1 is int:
        if int(num1) in dic1:
            print("Yes")
    else:
        print("No")


def targil3():
    dic1 = {1: 10, 2: 20, 3: 30, 4: 40, "a": 45, 5: "Roy"}
    dic2 = {}
    list1 = list(dic1)
    c = -1
    for i in dic1.values():
        c += 1
        print(c)
        dic2[i] = list1[c]
    print(dic2)


def targil4():
    limit = int(input("First Num: "))
    dic1 = {}
    for i in range (1, limit+1):
        dic1[i] = i**2
    print(dic1)


def targil5():
    dic1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
    print(sum(dic1.values()))


def targil6():
    num1 = int(input("Key to delete: "))
    dic1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
    del dic1[num1]
    print(dic1)


def targil7():
    # dic1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 40, 4: 50}
    # dic2 = {}
    # set1 = set(dic1)
    # set2 = set(dic1.values())
    # set2 = sorted(set2)
    # list1 = list(set1)
    # list2 = list(set2)
    # print(list1)
    # print(list2)
    # c = -1
    # for i in list1:
    #     c += 1
    #     dic2[i] = list2[c]
    # print(dic2)

    dic1 = {1: 10, 2: 20, 9: 5, 4: 40, 5: 50, 6: 40, 7: 50}
    dic2 ={}

    for i in dic1:
        if dic1[i] not in dic2.values():
            dic2[i] = dic1[i]
    print(dic2)


def targil8():
    names = ["Roy", "Shlomi", "Hasin", "Gilad", "Ziv"]
    grades = [100, 70, 95, 85, 60]
    dic1 = {}
    for i in range(5):
        dic1[names[i]] = grades[i]
    print(dic1)
    avg = (sum(grades) / 5)
    print("The average grade is: ", avg)
    list1 = []
    for name, grade in dic1.items():
        if grade >= avg:
            list1.append(name)
    print(list1)


targil8()






def targil5_test2():
    name = input("Enter name: ")
    for i in (name):
        a = name.count(i)
        if a <= 1:
            print("not two numbers")

        else:
            print(i)
            break
