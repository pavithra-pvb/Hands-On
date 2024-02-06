# Write your lots_of_math function here:
def lots_of_math(a,b,c,d):
  first = a + b
  print(first)
  second = c - d
  print(second)
  third = first * second
  print(third)
  return third % a
# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0