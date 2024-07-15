while node2 is not None:
  if node2.get_value() == val2:
    break
  node2_prev = node2
  node2 = node2.get_next_node()