class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def add_new_head(self, new_head_node):
        # --------> what line of code goes here?
        new_head_node.next_node = self.head_node
        self.head_node = new_head_node