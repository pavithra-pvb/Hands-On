#Write your function here
def add_greetings(names):
  names_list = []
  for name in names:
    names_list.append("Hello, " + name)
  return names_list

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))