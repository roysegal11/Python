def f_sum(a):
    for i in range(1, a):
        a += i
    return a


for i in range(5):
    num1 = int(input("Number: "))
    print(f_sum(num1))

print("How do I look? 1,000,000 $")
