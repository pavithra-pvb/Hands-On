#Write your function here
def larger_sum(lst1, lst2):
  list1 = 0
  list2 = 0
  for num in lst1:
    list1 += num
  for num in lst2:
    list2 += num
  if list1 >= list2:
    return lst1
  else:
    return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))