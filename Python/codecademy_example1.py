def divide_two_numbers(x, y):
  result = x / y
  return result

try:
  result = divide_two_numbers(2,0)
  print(result)
except NameError:
  print("A NameError occurred.")
except ValueError:
  print("A ValueError occurred.") 
except ZeroDivisionError:
  print("A ZeroDivisionError occurred.")