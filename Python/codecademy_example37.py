celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [temperature_in_celsius * 9/5 + 32 for temperature_in_celsius in celsius]
print(fahrenheit)