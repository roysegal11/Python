num1 = int(input("Enter number: "))

if 100 <= num1 <= 999:
    print((num1%1000//100)+(num1%100//10)+(num1%10))
else:
    print("Error")



#left = num1%1000//100

#mid = num1%100//10

#right = num1%10
