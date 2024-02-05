year = 2023


def find_century():
    global year
    return (year - 1) // 100 + 1


print(find_century())
