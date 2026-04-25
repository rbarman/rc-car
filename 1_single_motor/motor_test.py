from gpiozero import OutputDevice
from time import sleep

# IN1 is connected to GPIO 17
motor_pin = OutputDevice(17)

print("Motor spinning...")
motor_pin.on()
sleep(2)
motor_pin.off()
print("Motor stopped.")