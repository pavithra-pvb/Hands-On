a = 10
b = 20
def change():
    global b
    a = 45
    b = 56
change()
print(a)
print(b)

"""
Ans:
A) 10 56 - Ans
B) 10 45
C) 45 56
D) 10 20
"""