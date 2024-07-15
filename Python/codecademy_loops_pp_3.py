words = ['quite', 'nice', 'really']

for word in words:
    for letter in word:
        if not letter in 'aeiou':
            print(letter, end='')
    print()