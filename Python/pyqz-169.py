def greetings():
    return "Hi There!!!"
def greetings(name):
    return f"Hi {name}!"

print(greetings())

"""
Ans:
A) Hi {name}!
B) NameError
C) TypeError - Ans - TypeError: greetings() missing 1 required positional argument: 'name'
D) UnboundLocalError
"""