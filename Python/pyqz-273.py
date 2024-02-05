# print((lambda x, y:x + y, x * y)(12, 12)) - buggy code
print((lambda x, y: [x + y, x * y])(12, 12))


"""
Ans:
A) 12
B) 24
C) Error - Ans - NameError: name 'x' is not defined - for buggy code
D) 144
"""