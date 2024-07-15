numbers = [1, 2, 3, 4, 5, 6]
odds = []

for num in numbers:
    if num % 2 == 0:
        continue
    else:
        print(str(num) + " is odd")
        odds.append(num)