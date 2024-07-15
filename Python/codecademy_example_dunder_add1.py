class Atom:
    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return self.label

    def __add__(self, other):
        return Molecule([self, other])


class Molecule:
    def __init__(self, atoms):
        if type(atoms) is list:
            self.atoms = atoms

    def __repr__(self):
        return str(self.atoms)


sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
print("Original Salt: " + str(salt))
newsalt = sodium + chlorine
print("New Salt: " + str(newsalt))