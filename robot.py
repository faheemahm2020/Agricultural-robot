import RPi.GPIO as GPIO
import time

# Define motor control pins
motor1_in1 = 17  # IN1 for motor 1
motor1_in2 = 27  # IN2 for motor 1
motor2_in1 = 22  # IN3 for motor 2
motor2_in2 = 23  # IN4 for motor 2

# Set the GPIO pin for the relay (pump)
relay_pin = 13  # GPIO pin for the pump relay

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1_in1, GPIO.OUT)
GPIO.setup(motor1_in2, GPIO.OUT)
GPIO.setup(motor2_in1, GPIO.OUT)
GPIO.setup(motor2_in2, GPIO.OUT)
GPIO.setup(relay_pin, GPIO.OUT)


try:
# Move forward
GPIO.output(motor1_in1, GPIO.LOW)
GPIO.output(motor1_in2, GPIO.HIGH)
GPIO.output(motor2_in1, GPIO.LOW)
GPIO.output(motor2_in2, GPIO.HIGH)

print("Moving Forward")
time.sleep(10)  # Move forward for 5 seconds

# Stop the motors
GPIO.output(motor1_in1, GPIO.LOW)
GPIO.output(motor1_in2, GPIO.LOW)
GPIO.output(motor2_in1, GPIO.LOW)
GPIO.output(motor2_in2, GPIO.LOW)
print("Stopping. Turning Pump ON.")

# Turn on the pump
GPIO.output(relay_pin, GPIO.LOW)  # Assuming HIGH activates the pump
time.sleep(10)  # Keep the pump on for 2 seconds

# Turn off the pump
GPIO.output(relay_pin, GPIO.HIGH)   # Turn off the pump
print("Pump OFF")

# Move forward
GPIO.output(motor1_in1, GPIO.LOW)
GPIO.output(motor1_in2, GPIO.HIGH)
GPIO.output(motor2_in1, GPIO.LOW)
GPIO.output(motor2_in2, GPIO.HIGH)

print("Moving Forward")
time.sleep(10)  # Move backward for 5 seconds

# Stop the motors
GPIO.output(motor1_in1, GPIO.LOW)
GPIO.output(motor1_in2, GPIO.LOW)
GPIO.output(motor2_in1, GPIO.LOW)
GPIO.output(motor2_in2, GPIO.LOW)
print("Stopping. Turning Pump ON.")

# Turn on the pump again
GPIO.output(relay_pin,GPIO.LOW)  # Assuming HIGH activates the pump
time.sleep(10)  # Keep the pump on for 2 seconds

# Turn off the pump
GPIO.output(relay_pin,GPIO.HIGH)   # Turn off the pump
print("Pump OFF")

except KeyboardInterrupt:
pass

finally:
# Cleanup GPIO settings
GPIO.cleanup()
