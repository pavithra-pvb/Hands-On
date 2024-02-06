def who_am_i(income, own_business, investments):
    if income > 50000 or own_business:
        return "Enterpreneur"
    elif investments and not own_business:
        return "Investor"
    else:
        return "Employee"
    
print(who_am_i(40000, False, True))

#Ans:

#A) Enterpreneur
#B) Investor - Ans
#C) Employee