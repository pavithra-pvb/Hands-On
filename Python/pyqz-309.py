a = {'name' : 'abc'}
b = a
c = a.copy()
a['name'] = 'xyz'
print(b['name'], c['name'])

"""
Ans:

A: abc, abc
B: xyz, xyz
C: abc, xyz
D: xyz, abc - Ans

"""