#Write your function here

def odd_indices(lst):
  my_list = []
  for index in range(1, len(lst), 2):
    my_list.append(lst[index])
  return my_list

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))