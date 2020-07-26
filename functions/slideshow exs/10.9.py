list1 = []
num1 = input("Number: ")
long = len(num1)
int(num1)
print("Long:", long)

for i in range(1, long + 1):
    list1.append(num1[i - 1])

print(list1)
sum1 = 0
for i in list1:
    if int(i) % 2 == 0:
        sum1 = sum1 + int(i)

print(sum1)
