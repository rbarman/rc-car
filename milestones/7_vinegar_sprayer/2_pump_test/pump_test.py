from gpiozero import OutputDevice
from time import sleep

# Same relay IN pin as step 1 (GPIO 24) — now switching the pump instead of just clicking
pump_relay = OutputDevice(24)

print("Before running: intake tubing must be sitting in a cup of water,")
print("and the outlet should be pointed into a bowl or sink.")
input("Press Enter when ready...")

print("Pump ON")
pump_relay.on()
sleep(3)

print("Pump OFF")
pump_relay.off()
print("Done.")
