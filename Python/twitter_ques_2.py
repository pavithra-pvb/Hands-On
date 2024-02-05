def my_func(n):
    if n == 1:
        return 1
    else:
        return n * my_func(n - 1)


result = my_func(5)
print(result)
