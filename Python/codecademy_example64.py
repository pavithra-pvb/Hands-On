def get_length(string):
  count = 0
  for letter in string:
    count += 1
  return count

new_string = "Pavithra"
print(get_length(new_string))