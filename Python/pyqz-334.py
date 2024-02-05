my_list = [1, 2, 3, 4, 5, 6]
reduced_list = my_list[::2], # comma is causing error
reduced_list[0] = 10 #TypeError: 'tuple' object does not support item assignment

print(reduced_list)

""" 
Ans:

A) [10, 3, 5] - Ans, if comma is removed
B) Error - Ans
C) [10, 3]
D) [3, 5]
"""