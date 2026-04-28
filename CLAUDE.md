# RC Car Project

## Goal
Build a 4-wheel RC car controlled by a Raspberry Pi.

## Hardware

| Component | Details |
|---|---|
| Controller | Raspberry Pi 4 |
| Motor drivers | 1x L298N (both sides, two channels) |
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

- Battery red wire → L298N **+12V terminal** (motor power input, accepts 5-12V)
- Common ground rail connects Pi GND (pin 9), L298N GND terminal, and battery pack
- Left L298N drives front-left + back-left motors (wired in parallel)
- Right L298N drives front-right + back-right motors (wired in parallel)

## Milestones

| Folder | Goal | Status |
|---|---|---|
| `1_single_motor/` | One motor spinning via GPIO 17 | Done |
| `2_two_motors/` | Two motors wired in parallel to OUT1/OUT2, same on/off script | Done |
| `3_forward_reverse_stop/` | Add IN2 (GPIO 27) for direction control — forward, reverse, stop | Done |
| `4_four_motors/` | Add right side motors via Channel B (GPIO 22, 23 → IN3, IN4) | In progress |

## Pi GPIO Pinout (Raspberry Pi 4B rev 1.2)

```
   3V3  (1)  (2)  5V
 GPIO2  (3)  (4)  5V
 GPIO3  (5)  (6)  GND
 GPIO4  (7)  (8)  GPIO14
   GND  (9)  (10) GPIO15
GPIO17 (11)  (12) GPIO18   ← blue wire (IN1, Channel A)
GPIO27 (13)  (14) GND      ← white wire (IN2, Channel A)
GPIO22 (15)  (16) GPIO23   ← green (IN3, Ch B) / yellow (IN4, Ch B)
   3V3 (17)  (18) GPIO24
GPIO10 (19)  (20) GND
 GPIO9 (21)  (22) GPIO25
GPIO11 (23)  (24) GPIO8
   GND (25)  (26) GPIO7
 GPIO0 (27)  (28) GPIO1
 GPIO5 (29)  (30) GND
 GPIO6 (31)  (32) GPIO12
GPIO13 (33)  (34) GND
GPIO19 (35)  (36) GPIO16
GPIO26 (37)  (38) GPIO20
   GND (39)  (40) GPIO21
```

Pi is a **Raspberry Pi 4B rev 1.2**, BCM2711 SoC, 4GB RAM.

## SSH Access
```
ssh driver@rc-car.local
```

> **Tip:** Run `pinout` while SSH'd into the Pi to see a visual layout of the GPIO pins.

## Images
- `1_single_motor/single_motor_setup.jpg` — initial single-motor bench setup