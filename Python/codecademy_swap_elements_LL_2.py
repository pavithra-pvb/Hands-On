if node2_prev is None:
  input_list.head_node = node1
else:
  node2_prev.set_next_node(node1)