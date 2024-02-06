def my_family(age):
    family = {
        'Dad': range(40, 100),
        'Mom': range(50),
        'Child': range(0, 18)
    }

    for member, age_range in family.items():
        if age in age_range:
            return member
        
    return "Unknown"

print(my_family(45))

#Ans:
#A) Mom
#B) Dad - Ans
#C) Child
#D) Unknown