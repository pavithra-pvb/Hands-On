class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def remove_node(self, node_to_remove):
        current_node = self.head_node
        if current_node == node_to_remove:
            self.head_node = current_node.next_node
        else:
            while current_node:
                next_node = current_node.next_node
                if next_node == node_to_remove:
                    # --------> what line of code goes here?
                    current_node.next_node = next_node.next_node
                    current_node = None
                else:
                    current_node = next_node