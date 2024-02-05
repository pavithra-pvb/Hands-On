#Write your function here
def same_values(lst1, lst2):
  my_list = []
  for index in range(len(lst1)):
    if (lst1[index] == lst2[index]):
      my_list.append(index)
  return my_list


#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))