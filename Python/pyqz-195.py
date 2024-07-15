def func(item):
    if isinstance(item, list):
        item[0] = 2
        return item
    return item

values = ([1, 2, 3])

print(func(values))

"""
Ans:

A) ([1, 2, 3])
B) [2, 2, 3] - Ans
C) [1, 2, 3]
D) Error

"""