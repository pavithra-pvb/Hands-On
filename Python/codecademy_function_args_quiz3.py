def unite_args(*args):
    new_string = ""
    for arg in args:
        new_string += arg
    return new_string


print(unite_args("I'm ", "here ", "for ", "this "))