def Rishoni(a):
    for i in range (2, a):
        if a % i == 0:
            return (a,"Is not a prime number")
    else:
        return (a, "Is a prime number")

num1 = int(input("Enter Number: "))
print(Rishoni(num1))
