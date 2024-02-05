# List comprehension calling a function

from random import randint
random_numbers = [randint(number, 2 * number) for number in range(10)]
print(random_numbers)