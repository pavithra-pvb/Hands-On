class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def sum_tree(self):
        total = self.value
        for child in self.children:
            total += child.sum_tree()
        return total
    
root = Tree(10)
child1 = Tree(5)
child2 = Tree(3)
child3 = Tree(2)
child4 = Tree(8)

root.add_child(child1)
root.add_child(child2)
root.add_child(child3)
root.add_child(child4)

result = root.sum_tree()
print(result)

"""
Ans:

A) O(1)
B) O(n) - Ans
C) O(log n)
D) O(n^2)
"""