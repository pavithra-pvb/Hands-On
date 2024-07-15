s1 = {10, 20, 30, 40, 50}
s2 = {10, 20, 30, 40, 50}
s3 = {*s1, *s2}
print(s3)

"""
Ans:
{40, 10, 50, 20, 30}
* before s1 & s2 means unpacking the elements
"""