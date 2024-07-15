from products import create_product

def create_products(**products_dict):
  for name, price in products_dict.items():
    create_product(name, price)

new_product_dict = {
  'Apple': 1,
  'Ice Cream': 3,
  'Chocolate': 5,
}

# Call create_products() by passing new_product_dict
# as kwargs!
create_products(**new_product_dict)
