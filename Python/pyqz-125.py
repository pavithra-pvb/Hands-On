class Base:
    def __init__(self):
        self.__x = 4
        self.y = 2

    def display(self):
        print(self.__x, self.y)

class Child(Base):
    def __init__(self):
        super().__init__()
        self.__x = 5
        self.y = 9

obj = Child()
obj.display()

#Ans:

#A) 4 9 - Ans
#B) 5 9
#C) 4 2
#D) 5 2