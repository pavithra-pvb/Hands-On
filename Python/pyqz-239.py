silly_tuple = (["one", "two"], ["three"])
silly_tuple[1] += ["four"]
print(silly_tuple)

"""
Ans:
A) (['one','two'], ['four'])
B) (['one', 'two', 'three'], ['four'])
C) (['one', 'two'], ['three', 'four'])
D) None of the above - Ans: TypeError: 'tuple' object does not support item assignment
"""
