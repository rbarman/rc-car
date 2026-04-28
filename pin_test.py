from gpiozero import OutputDevice

PINS = {
    "1": (17, "IN1 - Channel A (blue wire)"),
    "2": (27, "IN2 - Channel A (white wire)"),
    "3": (22, "IN3 - Channel B (green wire)"),
    "4": (23, "IN4 - Channel B (yellow wire)"),
}

devices = {key: OutputDevice(pin) for key, (pin, _) in PINS.items()}

print("Pin Tester — activate one pin at a time to identify connections")
print("Note: tires on the same channel will spin together (1+2 share Channel A, 3+4 share Channel B)")
print("Commands: 1-4 to activate a pin, 0 to turn all OFF, q to quit\n")

for key, (pin, label) in PINS.items():
    print(f"  {key} = GPIO {pin} ({label})")

print()

while True:
    cmd = input(">>> ").strip().lower()

    if cmd == "q":
        break
    elif cmd == "0":
        for d in devices.values():
            d.off()
        print("All pins OFF")
    elif cmd in PINS:
        for d in devices.values():
            d.off()
        pin, label = PINS[cmd]
        devices[cmd].on()
        print(f"GPIO {pin} ON ({label})")
    else:
        print("Invalid command")

for d in devices.values():
    d.off()
print("All pins OFF. Bye.")
