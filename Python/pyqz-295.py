def puzzling_fun(my_list):
    my_set = set(my_list)
    my_new_list = list(my_set)
    my_new_list.sort(key=my_list.index)
    return my_new_list

my_list = list('entrepreneurial')
print(puzzling_fun(my_list))

"""
Ans: ['e', 'n', 't', 'r', 'p', 'u', 'i', 'a', 'l']
"""