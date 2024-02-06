# Checkpoint 1
print("My name is {name} and I'm feeling {feeling}.".format(
	# add your arguments to .format()
  name="Pavithra",
  feeling="awesome today"
))

# Checkpoint 2
from products import create_product

# Update create_products() to take arbitrary keyword arguments
def create_products(**products_dict):
  for name, price in products_dict.items():
    create_product(name, price)

# Checkpoint 3
# Update the call to `create_products()` to pass in this dictionary as a series of keyword
create_products(
  Baseball='3',
  Shirt='14',
  Guitar='70'
)
