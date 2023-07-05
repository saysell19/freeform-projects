class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, motor_speed = 0, direction = 180 , sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count
    
    # Add the methods here!
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction
    
    def adjust_sensor(self, new_range):
        self.sensor_range = new_range
robot_1 = DriveBot()
# Use the methods here!

robot_1.adjust_sensor(20)
robot_1.control_bot(10, 180)
print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

robot_2 = DriveBot(35, 75, 25)
print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)

robot_3 = DriveBot(sensor_range=900)
print(robot_3.motor_speed)
print(robot_3.direction)
print(robot_3.sensor_range)

DriveBot.all_disabled = True
DriveBot.latitude = 40.7128
DriveBot.longitude = 74.0060

print(robot_1.all_disabled)
print(robot_3.latitude)
print(robot_2.longitude)