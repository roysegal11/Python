class Circle:
    def __init__(self, radios):
        self.radios = radios
        self.pi = 3.14

    def Circum(self):
        print(f'The circumference of a circle: {2 * self.pi * self.radios}')

    def Area(self):
        print(f'The area of the circle: {self.pi * self.radios}')


rad = int(input("Enter Radios: "))

circle1 = Circle(rad)
circle1.Circum()
circle1.Area()
