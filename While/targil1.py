num = int(input("Enter 3 digits number: "))

while True:
    if num >= 100 and num <= 999:
        print((num % 10 + num // 10 % 10 + num // 100))
    else:
        print("Error")
    num = int(input("Enter 3 digits number: "))

