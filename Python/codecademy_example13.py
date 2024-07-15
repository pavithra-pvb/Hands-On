def cost_ground_shipping(weight):
  if(weight <= 2):
    price_per_pound = 1.50
  elif(weight <= 6):
    price_per_pound = 3.00
  elif(weight <= 10):
     price_per_pound = 4.00
  else:
    price_per_pound = 4.75

  return 20 + (price_per_pound * weight)

print(cost_ground_shipping(8.4))

premium_ground_shipping = 125.00

def cost_drone_shipping(weight):
  if(weight <= 2):
    price_per_pound = 4.50
  elif(weight <= 6):
    price_per_pound = 9.00
  elif(weight <= 10):
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25
  
  return 0 + (price_per_pound * weight)

print(cost_drone_shipping(1.5))

def cheapest_method_and_cost(weight):
  ground = cost_ground_shipping(weight)
  premium = premium_ground_shipping
  drone = cost_drone_shipping(weight)

  if(ground < premium and ground < drone):
    method = "Standard Ground"
    cost = ground
  elif(premium < ground and premium < drone):
    method = "Premiun Ground"
    cost = premium
  else:
    method = "Drone Shipping"
    cost = drone

  print("The cheapest shipping method is %s with $%.2f shipping cost." % (method, cost))


cheapest_method_and_cost(4.7)
cheapest_method_and_cost(41.9)
cheapest_method_and_cost(0.5)