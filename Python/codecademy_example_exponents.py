#Write your function here

def exponents(bases, powers):
  my_list = []
  for base in bases:
    for power in powers:
      my_list.append(base ** power)
  return my_list

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))