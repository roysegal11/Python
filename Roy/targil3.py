name = (input("Enter your name: "))
correct_year = int(input("Enter correct year: "))
age = int(input("Enter your age: "))
future_year = int(input("Enter future year: "))

difference = future_year - correct_year
new_age = age + difference

print(name, ",Your age in", str(future_year), "will be", str(new_age))
