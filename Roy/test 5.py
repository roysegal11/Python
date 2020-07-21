salary = int(input("Your correct salary:"))
present = int(input("You raise percent:"))
p = (present/100+1)
print(str(p)+"*"+str(salary))
print("=")
new_salary = p*salary
print("Your new salary is: "+str(new_salary))
