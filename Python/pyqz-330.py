lst = [0, 1]
[lst.append(lst[k - 1] + lst[k - 2]) for k in range(2, 5)]
print(lst)

""" 
Ans:

A) [1, 2, 3, 4, 5]
B) [0, 1, 2, 3, 4]
C) [0, 1, 1, 2 ,3] - Ans
D) Error
"""