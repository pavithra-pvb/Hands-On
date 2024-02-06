def item_summer(*args):
    current_sum = 0
    for arg in args:
        current_sum += arg
    return current_sum


my_list = [5, 19, 23, 88]

item_summer(*my_list)