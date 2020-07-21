# day = int(input("Enter day: "))
# month = int(input("Enter month: "))
# year = int(input("Enter year: "))


# if 1 <= day <= 31 and 1 <= month <= 12 and 1950 <= year <= 2020:
# print((day),"/",(month),"/",(year%100))
# else:
# print("Invalid input")


# if 1 <= day <= 31:
#     d = str(day)
# else:
#     print("Invalid day input")
#
# if 1 <= month <= 12:
#     m = str(month)
# else:
#     print("Invalid month input")
#
# if 1950 <= year <= 2020:
#     y = str(year % 100)
# else:
#     print("Invalid year input")
#
# if 1 <= day <= 31 and 1 <= month <= 12 and 1950 <= year <= 2020:
#     print(d + "/" + m + "/" + y)
# else:
#     print("Try again")



day = int(input("enter a day: "))
while day < 1 or day >31:
        print("the day is not true")
        day = int(input("enter a day: "))

month = int(input("enter a month: "))
while month < 1 or month >12:
     print("the month is not true")
     month = int(input("enter a month: "))

year = int(input("enter a year: "))
while year < 1950 or year >2020:
     print("the year is not true")
     year = int(input("enter a year: "))

print("the date is: ", day, "/",month, "/",year%100)
print("the date is: "+ str(day) + "/" + str(month) + "/" + str(year%100))
print("The date is: %d/%d/%d" %(day,month,year%100,))