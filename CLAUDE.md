# RC Car Project

## Goal
Build a 4-wheel RC car controlled by a Raspberry Pi.

## Hardware

| Component | Details |
|---|---|
| Controller | Raspberry Pi 4 |
| Motor drivers | 2x L298N (one per side) |
| Motors | 4x TT motors (yellow, with wheels) |
| Pi power | Wall outlet (USB) |
| Motor power | External battery pack → L298N boards |

## Wiring (GPIO → Driver)

| GPIO | Pin | Driver | Function |
|---|---|---|---|
| GPIO 17 | IN1 | Left L298N | Left motor forward/back |
| GPIO 27 | IN2 | Left L298N | Left motor forward/back |
| GPIO 22 | IN1 | Right L298N | Right motor forward/back |
| GPIO 23 | IN2 | Right L298N | Right motor forward/back |

- Common ground rail connects Pi GND (pin 9), both L298N boards, and battery pack
- Left L298N drives front-left + back-left motors (wired in parallel)
- Right L298N drives front-right + back-right motors (wired in parallel)

## Milestones

| Folder | Goal | Status |
|---|---|---|
| `1_single_motor/` | One motor spinning via GPIO 17 | Done |
| `2_two_motors/` | Two motors on one L298N, forward/reverse/stop | In progress |

## SSH Access
```
ssh driver@rc-car.local
```

## Images
- `1_single_motor/single_motor_setup.jpg` — initial single-motor bench setup