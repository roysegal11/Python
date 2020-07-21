num1 = int(input("Enter 3 digits number: "))
print(num1)
last = num1%1000//100
print(last)
mid = num1%100//10
print(mid)
firs = num1%10
print(firs)
print("backwords number: "+str(firs)+str(mid)+str(last))
