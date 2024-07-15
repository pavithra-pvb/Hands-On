class Car():
    def __init__(self, make, color):
        self.make = make
        self.color = color

class Sedan(Car):
    def honk(self):
        print("Beep Beep!")

civic = Sedan("honda", "silver")
#civic = Sedan()
#civic = Sedan(Car)
#civic = Car("honda", "silver")
print("Civic Value: ", type(civic))