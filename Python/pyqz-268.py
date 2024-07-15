lst = ['desert', 'dessert', 'to', 'too', 'lose', 'loose']
s = 'Mumbai'
i = 0
while i < len(lst):
    if i > 3:
        break
    else:
        print(i, lst[i], s[i])
    i += 1

    
"""
Ans:
0 desert M
1 dessert u
2 to m     
3 too b
"""