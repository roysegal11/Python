class Tamaguchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5

    def __str__(self):
        return f'The name of the animal is \"{self.name}\" The hunger level is {self.hunger} out of 10, and the energy level is {self.energy} out of 10'

    def Eat(self):
        food_gram = int(input("Food in Grams: "))
        sum_food = int(food_gram / 50)
        count = 0

        for i in range(sum_food):
            self.hunger -= 1
            count += 1
            messege = 0
            if self.hunger == -1:
                self.hunger += 1
                messege = 1
                break
        for i in range(int(count * 50 / 100)):
            self.energy -= 1

        if messege == 1:
            self.hunger = 0
            print(self.name, "is satisfied but did not eat all the food")

    def Play(self):
        minutes = int(input("Enter play time: "))
        sum_minutes = 0
        count = 0

        for i in range(minutes):
            sum_minutes = sum_minutes + 1
            if sum_minutes >= 10:
                count += 1
                self.energy -= 2
                sum_minutes -= 10
                messege = 0
                if self.energy == -1:
                    self.energy += 1
                    messege = 1
                    break
        for i in range(count):
            self.hunger += 2

        if messege == 1:
            print(self.name, "is too tired")

    def Rest(self):
        resting = int(input("Rest time: "))
        sum_rest = 0
        count = 0
        messege = 0
        for i in range(resting):
            sum_rest += 1
            if sum_rest == 20:
                self.energy += 1
                sum_rest -= 20
                if self.energy >= 10:
                    messege = 1
                    break
        for i in range(resting):
            sum_rest += 1
            if sum_rest == 30:
                self.hunger += 1
                sum_rest -= 30
                if self.hunger >= 10:
                    messege = 2
                    break
        if messege == 1:
            print(self.name, "rest enough and wonna play")
        else:
            pass
        if messege == 2:
            print(self.name, "is hungry")
        else:
            pass


name = input("Enter name")
dog = Tamaguchi(name)
print(dog)
print("1-Eat 2-Play 3-Rest 0-Exit")
command = int(input("Choose Action: "))
while command != 0:
    if command == 1:
        dog.Eat()
        print(dog)
        command = int(input("Choose Action: "))
    if command == 2:
        dog.Play()
        print(dog)
        command = int(input("Choose Action: "))
    if command == 3:
        dog.Rest()
        print(dog)
        command = int(input("Choose Action: "))

print("Thanks for playing! see you next time :)")
