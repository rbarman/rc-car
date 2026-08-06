from gpiozero import OutputDevice
from time import sleep

# IN is connected to GPIO 24
relay = OutputDevice(24)

print("Relay ON — listen for a click / check the relay's onboard LED")
relay.on()
sleep(2)

print("Relay OFF")
relay.off()
sleep(2)

print("Relay ON again")
relay.on()
sleep(2)

relay.off()
print("Done. Relay OFF.")
