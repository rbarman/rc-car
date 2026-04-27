import sys
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

commands = {"f": forward, "r": reverse}

if len(sys.argv) != 2 or sys.argv[1] not in commands:
    print("Usage: python3 motor_test.py [f|r]")
    sys.exit(1)

commands[sys.argv[1]]()
print(f"Motors: {'forward' if sys.argv[1] == 'f' else 'reverse'}")
sleep(2)
stop()
print("Motors: stop")
