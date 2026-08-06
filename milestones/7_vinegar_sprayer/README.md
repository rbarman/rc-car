# Milestone 7: Vinegar Sprayer

**Status:** Planning — parts not yet purchased.

## Goal
Drive the car onto the patio and spot-spray vinegar on weeds growing between bricks, triggered manually from the web controller. Autonomous weed detection/driving is a later phase (see `BACKLOG.md` in the project root).

## Why a diaphragm pump
Considered a diaphragm pump, a peristaltic pump, and a servo-actuated trigger sprayer. Diaphragm pump won because it builds real pressure, so a brief burst from a nozzle can cover a weed and the surrounding crack as the car passes by — a peristaltic pump's slow trickle would require parking precisely over each weed for several seconds, which doesn't suit a driving robot.

## Parts (not yet purchased)

| Part | Spec | Approx cost |
|---|---|---|
| Pump | 12V micro diaphragm pump, self-priming (e.g. "R385"/"365"-style) | $10-15 |
| Nozzle | Small fan/mist spray nozzle, barbed for tubing | $3-8 |
| Reservoir | 250-500mL bottle | $0-5 |
| Tubing | Vinegar-safe silicone or PVC | $3-5 |
| Relay | Single-channel 5V logic relay module | $3-6 |

## Wiring plan
- GPIO 24 → relay signal input (free pin — no conflict with motor GPIOs 17/27/22/23)
- Relay switches the pump off the existing motor battery pack — no separate battery needed: GPIO HIGH = pump on, GPIO LOW = off
- Ground is already shared via the existing motor battery/Pi ground rail
- Tubing routed away from the Pi and L298N so drips/leaks can't reach the electronics
- If bench testing shows voltage sag or motor stutter when the pump kicks on, split the pump onto its own separate battery instead

## Software plan
- Add a "Spray" button to `controller/app.py`, same hold-to-activate pattern as the existing drive buttons (hold = GPIO 24 HIGH, release = LOW)

## Next steps
1. Order parts
2. Wire relay + pump on the bench, verify on/off control from a GPIO test script (same pattern as `pin_test.py`)
3. Mount pump/reservoir/tubing on the chassis
4. Add "Spray" button to the web controller
5. Test on the patio
