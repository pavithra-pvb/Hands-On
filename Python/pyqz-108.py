class MyClass:
    def __init__(self, my_var):
        self.my_var = my_var

    def instance_method(self):
        self.my_var = 30
        return f"{self.my_var}"
    
obj = MyClass(10)
obj.instance_method()

print(obj.my_var)

#Ans:

#A) 30 - Ans
#B) 10
#C) 40
#D) Error