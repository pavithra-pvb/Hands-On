def func(x, y=None):
    if y is None:
        y = [1]
    y.extend(x)
    return y
print(func([0], [2, 4, 5]))

#Ans:

#A) [2, 4, 5, [0]]
#B) [1, 2, 4, 5, [0]]
#C) [0, 1, 2, 4, 5]
#D) [2, 4, 5, 0] - Ans
    
