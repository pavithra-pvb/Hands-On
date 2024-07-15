def add_one(x):
    return x + 1
d = {'a': 1, 'b': 2, 'c': 3}

result = map(add_one, d.values())
print(list(result))

"""
Ans:
A) [2, 3, 4] - Ans
B) (2, 3, 4)
C) [1, 2, 3]
D) [2, 3]

"""