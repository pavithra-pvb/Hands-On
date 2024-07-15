def func(x, y=[4, 3]):
    y.append(x)
    return y
print(func(2, [3, 4]))

#Ans:

#A) [3, 4, 2] - Ans
#B) [4, 3, 2]
#C) [2, 3, 4]
#D) None