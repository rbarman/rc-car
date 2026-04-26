from gpiozero import OutputDevice
from time import sleep

# IN1 connected to GPIO 17 — both motors wired in parallel to OUT1/OUT2
motor_pin = OutputDevice(17)

print("Motors spinning...")
motor_pin.on()
sleep(2)
motor_pin.off()
print("Motors stopped.")
