def mixed_func(str1, nada, nested):
    return not str1 if str1 or nada else nested
print(mixed_func("", None, [[]]))