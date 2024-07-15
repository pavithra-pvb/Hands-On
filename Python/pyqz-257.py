def hurried_func(num):
    t1 = bool(num%1)
    t2 = bool((num / 2) % 1)
    return 'EON'[t1 + t2]
print(
    hurried_func(2.5),
    hurried_func(70),
    hurried_func(19)
)

"""
Ans: N E O
"""