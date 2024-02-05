a = {1, 2, 3}
b = {1, 2, 3}

print(*(a + b))
#print(*(a | b)) - #Ans 1 2 3

#Ans:

#A) {2, 4, 6}
#B) [2, 4, 6]
#C) Error - Ans: TypeError: unsupported operand type(s) for +: 'set' and 'set'
#D) [1, 2, 3]