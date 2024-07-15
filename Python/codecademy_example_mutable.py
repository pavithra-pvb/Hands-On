def update_order(new_item, current_order=[]):
  current_order.append(new_item)
  return current_order
 
# First order, burger
order1 = update_order({'item': 'burger', 'cost': '3.50'})
 
# Second order, just a soda
order2 = update_order({'item': 'soda', 'cost': '1.50'})
 
# What's in that second order again?
print(order2)