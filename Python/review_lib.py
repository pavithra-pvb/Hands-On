import random

def get_next_review():
  if random.random() > .5:
    return None
  else:
    return "5/5 Stars, Incredible service and prompt response. Try the coffee!"

def submit_review(review):
  if review is None:
    raise Exception("Submission of an empty review!")
