d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

d = {key.upper() : value * 100 for (key, value) in d.items()}

print(d)

"""
Ans:

{'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500}
"""