import time
import board
import pwmio
import digitalio
from adafruit_motor import motor

# Set up the start button
start_button = digitalio.DigitalInOut(board.GP20)
start_button.direction = digitalio.Direction.INPUT
start_button.pull = digitalio.Pull.UP

# Set up the right motor
m1a = pwmio.PWMOut(board.GP8, frequency=10000)
m1b = pwmio.PWMOut(board.GP9, frequency=10000)
motor1 = motor.DCMotor(m1a, m1b)

# Set up the left motor
m2a = pwmio.PWMOut(board.GP10, frequency=10000)
m2b = pwmio.PWMOut(board.GP11, frequency=10000)
motor2 = motor.DCMotor(m2a, m2b)

# Set up the right sensor
right_sensor_pin = digitalio.DigitalInOut(board.GP26)
right_sensor_pin.direction = digitalio.Direction.INPUT

# Set up the left sensor
left_sensor_pin = digitalio.DigitalInOut(board.GP5)
left_sensor_pin.direction = digitalio.Direction.INPUT


# Define the line-following function
def line_follow():
    if right_sensor_pin.value == 0 and left_sensor_pin.value == 1: # Left sensor is above the line so turn left
        motor1.throttle = 0.3
        motor2.throttle = 0.0
    elif left_sensor_pin.value == 0 and right_sensor_pin.value == 1: # Right sensor is above the line so turn right
        motor1.throttle = 0.0
        motor2.throttle = -0.3

# Wait for start button to be checked
while True:
    if not bool(start_button.value):
        break

# Main loop
while True:
    motor1.throttle = 0.3
    motor2.throttle = -0.34
    if right_sensor_pin.value == 1 or left_sensor_pin.value == 1:
        line_follow()
        if right_sensor_pin.value == 1 and left_sensor_pin.value == 1: # Stop at the finish line
            motor1.throttle = 0.0
            motor2.throttle = -0.0

    time.sleep(0.01) 
    
