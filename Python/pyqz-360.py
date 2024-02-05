class Camera:
    def click(self):
        return "Clicking a photo"
    
class Computer:
    def compute(self):
        return "Computing tasks"
    
class Smartphone(Camera, Computer):
    pass

device = Smartphone()
print(device.click())
print(device.compute())

""" 
Ans:

A) Clicking a photo
   Computing tasks    - Ans
B) Clicking a photo
C) Computing tasks
D) None

"""