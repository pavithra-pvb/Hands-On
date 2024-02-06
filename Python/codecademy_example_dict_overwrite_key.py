oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners.update({"Supporting Actress":"Viola Davis"})
print(oscar_winners)

oscar_winners["Best Picture"] = "Moonlight"
print(oscar_winners)