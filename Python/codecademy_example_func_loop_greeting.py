#Write your function here

def add_greetings(names):
  my_list = []
  for name in names:
    my_list.append("Hello, " + name)
  return my_list
#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))