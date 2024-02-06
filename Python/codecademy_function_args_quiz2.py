def find_string(**kwargs):
  for keyword, arg in kwargs.items():
    print(arg.find(keyword))

find_string(waldo="long sentence with waldo in it")