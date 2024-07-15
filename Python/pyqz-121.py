def multipliers():
    return [lambda x, i=i: i * x for i in range(4)]

result = [m(2) for m in multipliers()]
print(result)

#Ans:

#A) [6, 6, 6, 6]
#B) [0, 2, 4, 6] - Ans
#C) Error
#D) [0, 1, 2, 3]