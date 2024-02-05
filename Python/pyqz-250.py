def func(x):
    if x <= 1:
        return 1
    else:
        return x * func(x - 1)
    
print(func(4))

"""
Ans:
A) 3
B) 24 - Ans
C) 4
D) 12
"""