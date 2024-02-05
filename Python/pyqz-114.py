class MyClass:
    def __init__(self, data: tuple or list):
        self.data = data
    
    def my_method(self):
        if isinstance(self.data, tuple):
            return self.data[1:][::-1]
        else:
            return self.data[::-3]
        
words = ['apple', 'banana', 'cherry']
obj = MyClass(words)

print(obj.my_method())
      
#Ans:

#A) ['cherry'] - Ans
#B) ('cherry')
#C) ['cherry', 'banana']
#D) ['cherry', 'banana', 'apple']