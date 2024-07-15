def fun(num):
    if num > 10:
        return num - 10
    return fun(fun(num + 11))

print(fun(5))

""" 
Ans:

A) 10
B) 9
C) 1 - Ans
D) 0
"""