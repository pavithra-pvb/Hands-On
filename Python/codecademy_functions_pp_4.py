def robot(battery_level=100, status="online", mood="happy", name="robo2000"):
  return "Hello, I am %s. I am currently %s at a battery level of %s%%. My mood today is %s." % (name, status, battery_level, mood)

print(robot(20, "offline", "tired"))
#print(robot("offline", 20, "tired"))
#print(robot(status="offline", mood="tired", 20))
#print(robot(battery_level=20, status="offline", "tired"))