from gpiozero import OutputDevice

# Relay IN pin — controls the pump, powered off its own dedicated battery
pump_relay = OutputDevice(24)

def spray_on():
    pump_relay.on()

def spray_off():
    pump_relay.off()
