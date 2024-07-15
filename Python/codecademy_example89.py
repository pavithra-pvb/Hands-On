// Break statement in Loops

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog in dog_breeds_available_for_adoption:
  print(dog)

  if dog == dog_breed_I_want:
    print("They have the dog I want!")
    break