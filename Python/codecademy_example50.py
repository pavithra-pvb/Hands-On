#Write your function here
def exponents(bases, powers):
  exponents_new = []
  for base in bases:
    for power in powers:
      exponents_new.append(base ** power)
  return exponents_new

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))