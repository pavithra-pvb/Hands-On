old = 0
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
for i in list1:
    list2.append(i + old)
    old = i
print(list2)