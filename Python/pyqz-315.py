def fun(a, *args, s = '!'):
    print(a, s)
    for i in args:
        print(i, a)

fun(100)

"""
Ans:

A) Error
B) 100 ! - Ans
C) ! 100
D) 100
"""