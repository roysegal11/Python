num1 = 0
count = 0
for i in range(6):
    num2 = int(input("Number: "))
    if num2%2==0:
        num1 = num1 + num2
        count+=1
    print(num1)
    print(count)
print(num1/count)