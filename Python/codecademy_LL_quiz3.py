class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node


a = Node(5)
b = Node(70, a)
c = Node(5675, b)
d = Node(90, c)
ll = LinkedList(d)

