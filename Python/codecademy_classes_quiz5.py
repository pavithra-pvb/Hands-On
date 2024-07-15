class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Hiya {}!".format(self.name)


devorah = User("Devorah")
print(devorah)