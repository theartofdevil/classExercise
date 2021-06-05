'''
#                       Example 1....
class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return self.pi*(self.radius**2)
    def circumfrence(self):
        return 2*self.pi*self.radius

class Square:
    def __init__(self,length):
        self.length = length
    def area(self):
        return self.length**2
    def circumfrence(self):
        return 4*self.length

radius = int(input("enter the circle radius : "))
length = int(input("enter the square's length"))

square = Square(length )
circle = Circle(radius)

square_area = square.area()
square_circumfrense = square.circumfrence()

circle_area = circle.area()
circle_circumfrence = circle.circumfrence()

print ('square area is '+format(square_area)+' and circumfrence is '+format(square_circumfrense))
print ('circle area is'+format(circle_area)+' circle circumfrence is '+format(circle_circumfrence))

'''

#                       Example 2..... ( inheritance)
'''
class Vehicle:
    # Class attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def writeType(self):
        print ("this is a vehicle ... ")
        
class Bus(Vehicle):
    def writeType(self):
        print ("this is a bus ... ")

class Car(Vehicle):
    def writeType(self):
        print ("this is a car ... ")

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)

'''


