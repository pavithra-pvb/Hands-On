def func(a, *args, s='!'):
    print(a, s)
    for i in args:
        print(i, s)

func(10)

"""
Ans:

A) 10 ! - Ans
B) 10!
C) ! 10
D) Error
"""