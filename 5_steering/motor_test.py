import sys
from gpiozero import OutputDevice
from time import sleep

# Channel A - right side
IN1 = OutputDevice(17)
IN2 = OutputDevice(27)

# Channel B - left side
IN3 = OutputDevice(22)
IN4 = OutputDevice(23)

def right_forward():  IN1.on();  IN2.off()
def right_reverse():  IN1.off(); IN2.on()
def right_stop():     IN1.off(); IN2.off()
def left_forward():   IN3.on();  IN4.off()
def left_reverse():   IN3.off(); IN4.on()
def left_stop():      IN3.off(); IN4.off()

COMMANDS = {
    "f":  (left_forward,  right_forward, "forward"),
    "r":  (left_reverse,  right_reverse, "reverse"),
    "tl": (left_stop,     right_forward, "turn left"),
    "tr": (left_forward,  right_stop,    "turn right"),
    "sl": (left_reverse,  right_forward, "spin left"),
    "sr": (left_forward,  right_reverse, "spin right"),
}

if len(sys.argv) != 2 or sys.argv[1] not in COMMANDS:
    print("Usage: python3 motor_test.py [f|r|tl|tr|sl|sr]")
    print("  f  = forward")
    print("  r  = reverse")
    print("  tl = turn left")
    print("  tr = turn right")
    print("  sl = spin left")
    print("  sr = spin right")
    sys.exit(1)

left_fn, right_fn, label = COMMANDS[sys.argv[1]]
left_fn()
right_fn()
print(f"Motors: {label}")
sleep(2)
left_stop()
right_stop()
print("Motors: stop")
