class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed=0, direction=180, sensor_range=10):
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

    # Override the + and - operations here!

    def __add__(self, value):
        self.speed += value

    def __sub__(self, value):
        self.speed -= value


class DriveBot(Robot):

    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        super().__init__(motor_speed, direction, sensor_range)

    # Override the + and - operations here while using those dunder methods from the superclass!

    def __add__(self, value):
        super().__add__(value)
        self.sensor_range += value

    def __sub__(self, value):
        super().__sub__(value)
        self.sensor_range -= value


class WalkBot(Robot):

    def __init__(self, steps_per_minute=0, direction=180, sensor_range=10, step_length=5):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length

    def adjust_sensor(self, new_sensor_range):
        super().adjust_sensor(new_sensor_range)
        self.obstacle_found = False
        self.step_length = 5

    def avoid_obstacles(self):
        if (self.obstacle_found):
            if (self.speed <= 60):
                super().avoid_obstacles()
            else:
                self.direction = (self.direction + 90) % 360
                self.obstacle_found = False
            self.speed /= 2
            self.step_length /= 2

    # Override the + and - operations here while using those dunder methods from the superclass!

    def __add__(self, value):
        super().__add__(value)
        self.step_length += value / 2

    def __sub__(self, value):
        super().__sub__(value)
        self.step_length -= value / 2


robot_1 = DriveBot()
robot_2 = WalkBot()

# Uncomment these lines when you are ready to test your code!
robot_1 + 20
robot_1 - 10
robot_2 + 10
robot_2 - 5

print(robot_1.speed)
print(robot_1.sensor_range)
print(robot_2.speed)
print(robot_2.step_length)