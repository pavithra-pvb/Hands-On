def my_func(value):
    if value == 5:
        return ["Python"]
    else:
        yield from range(value)

print(list(my_func(5)))

#Ans:

#A) ["Python"]
#B) [0, 1, 2, 3, 4]
#C) [] - Ans
#D) None of the above