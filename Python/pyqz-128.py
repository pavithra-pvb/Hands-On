D = {1 : 1, 2: '2', '1' : 2, '2' : 3}
D['1'] = 2
print(D[D[D[str(D[1])]]])

#Ans:

#A) 2
#B) 3 - Ans
#C) '2'
#D) Error