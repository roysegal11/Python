def t51():
    num1 = (input("Enter numbers: "))
    s = 0
    list1 = list(num1)
    print("The list:",list1)
    print("The high number:",max(list1))
    print("The low number:",min(list1))
    many = len(list1)
    for  i in range (len(list1)):
        s = s + int(list1[i])
    print("The avrage:",s/many)



def t52():
    letters = input("Type here: ")
    print(letters[::-1])



def t53():
    from random import randint
    list1 = []
    for i in range (10):
        num1 = randint(1, 10)
        list1.append(num1)
    print(list1)

    list2 = [randint(1,10) for i in range (10)]
    print(list2)



def t54():
    sen1 = input("list1:")
    sen2 = input("list2:")
    list1 = list(sen1)
    list2 = list(sen2)

    print((list1)+(list2))
    print(len(list1+list2))



def t55():
    list_grade = input("Enter grades: ")
    list1 = list_grade.split(" ")
    count = 0
    d_count = 0
    for i in range(len(list1)):
        grade = int(list1[i])
        if grade >= 60:
            count += 1
        else:
            d_count += 1
    print("pass:", count)
    print("Fail:", d_count)



def t56():
    list1 = list(range(1,11))
    print(list1)
    print(list1[7:11])
    print(list1[::-1])
    print(list1[1::2])
    print(list1[::2])

    # num1 = input("3 digit number: ")
    # list2 = list(num1)
    # list1[4] = list2[0]
    # list1[5] = list2[1]
    # list1[-1] = list2[2]
    # print(list1)

    #אפשרות 1
    list3 = [i * 2 for i in list1]
    print(list3)
    #אפשרות 2
    list4=[]
    for i in list1:
        i = (i*2)
        list4.append(i)
    print(list4)

    #אפשרות 1
    list5 = []
    list5.append(list1[0])
    list5.append(list1[-1])
    print(list5)
    #אפשרות 2
    list6 = [list1[0],list1[len(list1)-1]]
    print(list6)



