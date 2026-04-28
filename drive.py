from gpiozero import OutputDevice

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

def forward():
    left_forward()
    right_forward()

def reverse():
    left_reverse()
    right_reverse()

def turn_left():
    left_stop()
    right_forward()

def turn_right():
    left_forward()
    right_stop()

def spin_left():
    left_reverse()
    right_forward()

def spin_right():
    left_forward()
    right_reverse()

def stop():
    left_stop()
    right_stop()
