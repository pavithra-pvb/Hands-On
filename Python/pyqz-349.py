class A:
    answer = 42
    def __init__(self):
        self.answer = 21
        self.__add__ = lambda x, y : x.answer + y
    def __add__(self, y):
        return self.answer - y
print(A() + 5)

""" 
Ans:
A) 16 - Ans
B) 26
C) 47
D) None of these
E) Exception

"""