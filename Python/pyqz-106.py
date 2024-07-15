import math

#def math(number): - gives AttributeError: 'function' object has no attribute 'sqrt'
def square_root(number):
    return math.sqrt(number)

def main(number):
    print(f"The square root of {number} is {square_root(number)}")

main(8)

#Ans: 2.8284271247461903
