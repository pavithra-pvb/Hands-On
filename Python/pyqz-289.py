def my_func(x):
    if x == 0:
        return 0
    else:
        return x + my_func(x - 1)
    
print(my_func(5))

"""
Ans:
A) 0
B) 5
C) 10
D) 15 - Ans
"""