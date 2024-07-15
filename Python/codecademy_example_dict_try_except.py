caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

#caffeine_level["matcha"] = 30
key_to_check = "matcha"
try:
  print(caffeine_level[key_to_check])
except KeyError:
  print("Unknown Caffeine Level")