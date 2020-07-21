
def targil9():
    num1 = int(input("number"))
    for i in range(2,num1+1,2):
        print(i)
  
def targil10():
    num = int(input("Number: "))
    count = 0
    while num != 0:
        if num % 3 == 0 or num % 7 == 0:
            count += 1
        num = int(input("Number: "))

    print(count)


targil10()



