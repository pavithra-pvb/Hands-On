def func(arr: list):
    gen = (name for name in arr if len(arr) >= 3)
    arr = ["Jey", "Jimmy"]
    return list(gen)

arr = ["Joe", "Jey", "Solo"]

print(func(arr))

#Ans:

#A) ["Joe", "Jey", "Jimmy"]
#B) ["Jey", "Jimmy"]
#C) [] - Ans
#D) 3