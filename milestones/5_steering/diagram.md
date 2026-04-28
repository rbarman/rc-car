```mermaid
graph TD
    PiPower[Pi USB Power] --> Pi
    Batt[Battery Pack] -->|+12V terminal| D1
    Batt -->|GND| GND_Bus[Common Ground Rail]

    subgraph Pi [Raspberry Pi 4]
        GPIO17[GPIO 17 - blue wire]
        GPIO27[GPIO 27 - white wire]
        GPIO22[GPIO 22 - green wire]
        GPIO23[GPIO 23 - yellow wire]
        PiGND[GND - Pin 9]
    end

    PiGND --> GND_Bus
    GND_Bus -->|GND| D1

    subgraph D1 [L298N Driver]
        IN1[IN1]
        IN2[IN2]
        IN3[IN3]
        IN4[IN4]
        OUT_A[OUT1/OUT2 - Channel A - RIGHT side]
        OUT_B[OUT3/OUT4 - Channel B - LEFT side]
    end

    GPIO17 --> IN1
    GPIO27 --> IN2
    GPIO22 --> IN3
    GPIO23 --> IN4

    OUT_A --> MR[Right Motors x2 - FRONT_RIGHT & BACK_RIGHT]
    OUT_B --> ML[Left Motors x2 - FRONT_LEFT & BACK_LEFT]
```

## Steering Logic (Tank Steering)

| Command | Left Side | Right Side | Result |
|---------|-----------|------------|--------|
| f  | Forward | Forward | Straight |
| r  | Reverse | Reverse | Reverse |
| tl | Stop    | Forward | Turn left |
| tr | Forward | Stop    | Turn right |
| sl | Reverse | Forward | Spin left in place |
| sr | Forward | Reverse | Spin right in place |
