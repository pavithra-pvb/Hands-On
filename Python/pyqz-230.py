a = set()

for n in range(21, 30):
    if n % 2 == 0:
        a.add(n)
print(a)

# In one line
a = {n for n in range(21, 30) if n % 2 == 0}
print(a)
"""
Ans: {24, 26, 28, 22}
"""