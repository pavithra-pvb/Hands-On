def foo(x):
    try:
        return 10 / x
    except ZeroDivisionError:
        return "Error"
    finally:
        return 0
    
result = foo(0)
print(result)

#Ans:

#A) 0  - Ans
#B) "Error"
#C) 10
#D) This code will raise an exception