# Milestone 7: Vinegar Sprayer

**Status:** In progress — parts purchased, working through bench tests incrementally.

## Goal
Drive the car onto the patio and spot-spray vinegar on weeds growing between bricks, triggered manually from the web controller. Autonomous weed detection/driving is a later phase (see `BACKLOG.md` in the project root).

## Why a diaphragm pump
Considered a diaphragm pump, a peristaltic pump, and a servo-actuated trigger sprayer. Diaphragm pump won because it builds real pressure, so a brief burst from a nozzle can cover a weed and the surrounding crack as the car passes by — a peristaltic pump's slow trickle would require parking precisely over each weed for several seconds, which doesn't suit a driving robot.

## Parts

| Part | Spec | Status |
|---|---|---|
| Pump | 12V 300mA 1.2LPM micro self-priming diaphragm pump | Purchased |
| Nozzle | Fan/mist spray nozzle | Purchased |
| Tubing | Vinyl tubing | Purchased |
| Relay | 5V single-channel relay module, optocoupler isolation, H/L trigger select | Purchased |
| Reservoir | 250-500mL bottle | Any bottle on hand |

## Wiring plan
- GPIO 24 → relay signal input (free pin — no conflict with motor GPIOs 17/27/22/23)
- Relay switches the pump off the existing motor battery pack — no separate battery needed: GPIO HIGH = pump on, GPIO LOW = off
- Ground is already shared via the existing motor battery/Pi ground rail
- Tubing routed away from the Pi and L298N so drips/leaks can't reach the electronics
- If bench testing shows voltage sag or motor stutter when the pump kicks on, split the pump onto its own separate battery instead

## Software plan
- Add a "Spray" button to `controller/app.py`, same hold-to-activate pattern as the existing drive buttons (hold = GPIO 24 HIGH, release = LOW)

## Incremental steps

Going one new piece of hardware at a time, same style as milestones 1-5.

1. [`1_relay_test/`](1_relay_test/) — wire just the relay to the Pi (no pump/water), confirm GPIO 24 clicks it on/off — done
2. [`2_pump_test/`](2_pump_test/) — wire the pump through the relay off the battery pack, prime from a cup of water, confirm it pumps on command — **current step**
3. `3_nozzle_test/` — attach tubing + nozzle, check spray pattern over a sink/bucket
4. `4_mounting/` — mount pump/reservoir/tubing on the chassis, routed away from the Pi and L298N
5. `5_web_integration/` — add a "Spray" button to `controller/app.py`, same hold-to-activate pattern as the drive buttons
6. `6_field_test/` — test on the patio
