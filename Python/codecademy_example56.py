destinations=["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveller=['Erin Wilkies', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index=destinations.index(destination)
  return destination_index

print(get_destination_index("Los Angeles, USA"))

print(get_destination_index("Paris, France"))

#print(get_destination_index("Bangalore, India")) ----> Since this destination is not listed, it will give ValueError message during execution

def get_traveller_location(traveller):
  traveller_destination = traveller[1]
  traveller_destination_index=get_destination_index(traveller_destination)
  return traveller_destination_index

test_destination_index = 0
test_destination_index=(get_traveller_location(test_traveller))

print(test_destination_index)

attractions = []
for destination in destinations:
  attractions.append([])

print(attractions)

def add_attraction(destination, attraction):
  try:
      destination_index=get_destination_index(destination)
      attractions_for_destination=attractions[destination_index].append(attraction)
  except SyntaxError:
    return

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])

print(attractions)

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


def find_attractions(destination, interests):
  destination_index=get_destination_index(destination)
  attractions_in_city=attractions[destination_index]
  attractions_with_interest=[]

  for attraction in attractions_in_city:
    possible_attraction=attraction
    attraction_tags=attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

la_arts=find_attractions("Los Angeles, USA", ['art'])
print(la_arts)

def get_attractions_for_traveller(traveller):
  traveller_destination = traveller[1]
  traveller_interests = traveller[2]
  traveller_attractions = find_attractions(traveller_destination, traveller_interests)

  interests_string="Hi " + traveller[0] + ", we think you'll like these places around " + traveller_destination + ": " 
  for i in range(len(traveller_attractions)):
    if traveller_attractions[-1] == traveller_attractions[i]:
      interests_string += "the " + traveller_attractions[i] + "."
    else:
      interests_string += "the " + traveller_attractions[i] + ", "
    return interests_string

smills_france = get_attractions_for_traveller(['Dereck Smill', 'Paris, France', ['monument']])

print(smills_france)













