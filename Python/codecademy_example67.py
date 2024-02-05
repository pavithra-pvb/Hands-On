def username_generator(first_name, last_name):
  if(len(first_name)) < 3:
    username = first_name
  else:
    username = first_name[:3]

  if(len(last_name)) < 4:
    username += last_name
  else:
    username += last_name[:4]

  return username

def password_generator(username):
  password = ""

  for i in range(0, len(username)):
    password += username[i - 1]
  return password

print(username_generator("Abe", "Simpson"))
print(password_generator("Pavithra"))