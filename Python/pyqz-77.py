def foo(x, y=[]):
    y.append(x)
    return y

print(foo(2))
print(foo(3))

#Ans:

#A) [1,2,3]
#B) [1,2,3,4]
#C) [4]
#D) It will raise an error

#Actual Output - [2] [2, 3]