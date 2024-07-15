def unusual_func(x:list):
    if all(x):
        return "Hello"
    elif not x:
        return "Hi"
    else:
        return "Goodbye"
    
lst = [1, 2, -3, 4, 0]
print(unusual_func(lst))

"""
Ans:
A) Hello
B) Hi
C) Goodbye - Ans
D) Error
"""