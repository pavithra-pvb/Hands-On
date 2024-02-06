l=[1, 0, 2, 0, 'hello', '', []]
print(list(filter(bool, l)))


#Ans:
#A) [1. 0, 2, 'hello', ", []]
#B) [1, 2, 'hello'] - Ans
#C) Error
#D) [1, 0, 2, 0, 'hello', ", []]