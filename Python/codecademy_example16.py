# len() function examples

examples = ['red', 'yellow', 'orange', 'green']

print(len(examples))

for color in range(len(examples)):
	print(color)
	#print(examples[color])
	
employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']

index4 = (employees[4])

print(len(employees))

print(employees[6])

print(index4)

colors = ['red', 'green', 'blue', 'yellow', 'orange']

# List containing last 2 elements

print(colors[-2:])

# List excluding last 2 elements 

print(colors[:-2])

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

sublist = letters[1:7]

print(sublist)

letters = ['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']

num_i = letters.count('i')

print(num_i)

vehicles = ['car', 'scooter', 'lorry', 'truck', 'van', 'van', 'car', 'car']

cars = print(vehicles.count('car'))
vans = print(vehicles.count('van'))
buses = print(vehicles.count('bus'))

inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

inventory_len = len(inventory)

print(inventory_len)

first = inventory[0] 

print(first)

last = inventory[-1]

print(last)

inventory_2_6 =  inventory[2:6]

print(inventory_2_6)

first_3 = inventory[0:3]

print(first_3)

twin_beds = inventory.count("twin bed")

print(twin_beds)

inventory.sort()

print(inventory)