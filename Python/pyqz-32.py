from abc import ABC, abstractmethod

class Parent(ABC):
    def common(self):
        print("Parent")

    @abstractmethod
    def vary(self):
        pass

class Child(Parent):
    def vary(self):
        print("Child")

obj = Child()
obj.common()
obj.vary()

#Ans:

#A) Parent
#B) Parent Child - Ans
#C) Error
#D) Child Parent
