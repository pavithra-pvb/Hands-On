def outer_func(x):
    y = 1 + x
    def inner_func():
        x = 2
        def inner_inner():
            x = 3
            return x + y
        return inner_inner
    return inner_func

results = outer_func(4)
my_results = results()

print(my_results() + 2)

"""
Ans:
A) 8
B) 5
C) 10 - Ans
D) 4
"""