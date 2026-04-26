from gpiozero import OutputDevice
from time import sleep

IN1 = OutputDevice(17)
IN2 = OutputDevice(27)

def forward():
    IN1.on()
    IN2.off()

def reverse():
    IN1.off()
    IN2.on()

def stop():
    IN1.off()
    IN2.off()

print("Forward...")
forward()
sleep(2)

print("Stop...")
stop()
sleep(1)

print("Reverse...")
reverse()
sleep(2)

print("Stop.")
stop()
