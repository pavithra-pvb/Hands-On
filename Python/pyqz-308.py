a = set()

for n in range(21, 40):
    if n % 2 == 0:
        a.add(n)

print(a)

"""
Ans: {32, 34, 36, 38, 22, 24, 26, 28, 30}
"""

# set comprehension

a = {n for n in range(21, 40) if n % 2 == 0}

print(a)

"""
Ans: {32, 34, 36, 38, 22, 24, 26, 28, 30}
"""