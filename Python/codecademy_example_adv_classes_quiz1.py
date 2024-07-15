class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed = 0, direction = 180, sensor_range = 10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False

# Create the DriveBot class here!
class DriveBot(Robot):
  def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
    super().__init__(motor_speed, direction, sensor_range)
# Create the WalkBot class here!

class WalkBot(Robot):
  def __init__(self, steps_per_minute = 0, direction = 180, sensor_range = 10, step_length = 5):
    super().__init__(steps_per_minute, direction, sensor_range)
    self.step_length = step_length

# Uncomment the robot instantiation!
robot_1 = DriveBot()
robot_2 = WalkBot()
robot_3 = WalkBot(20, 90, 15, 10)

# Use these print statements to test your code!

print(robot_2.id)
print(robot_3.step_length)
print(robot_1.speed)

