class Person:
    def __init__(self, name, age, num_kids):
        self.name = name
        self.age = age
        self.num_kids = num_kids

    def __str__(self):
        return f"Your name is {self.name}, you are {self.age} years old, and you have {self.num_kids} kids"

    def Childer(self):
        if num_kids is not 0:
            print(name, "have children")
        if num_kids is 0:
            print(name, "do not have children")

    def Age_sec(self):
        if 0 < age <= 18:
            print(name, "Is Child")
        if 19 <= age <= 60:
            print(name, "Is Adult")
        if 61 <= age <= 120:
            print(name, "Is Senior")


name = input("Your name: ")
age = int(input("Your age: "))
num_kids = int(input("Number of children: "))

man1 = Person(name, age, num_kids)
print(man1)
man1.Childer()
man1.Age_sec()
