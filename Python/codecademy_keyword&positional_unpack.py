def remove(filename, *args, **kwargs):
    with open(filename) as file_obj:
        text = file_obj.read()

    # Add code here to update text.
    for arg in args:
        text = text.replace(arg, "")
    for kwarg, replacement in kwargs.items():
        text = text.replace(kwarg, replacement)
    return text


print(remove("text.txt", "generous", "gallant", fond="amused by", Robin="Mr. Robin"))