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
        OUT_A[OUT1/OUT2 - Channel A]
        OUT_B[OUT3/OUT4 - Channel B]
    end

    GPIO17 -->|IN1 - Channel A| IN1
    GPIO27 -->|IN2 - Channel A| IN2
    GPIO22 -->|IN3 - Channel B| IN3
    GPIO23 -->|IN4 - Channel B| IN4

    OUT_A --> ML[Left Motors x2]
    OUT_B --> MR[Right Motors x2]
```

## Pin Logic

| IN1 | IN2 | Left Motors | IN3 | IN4 | Right Motors |
|-----|-----|-------------|-----|-----|--------------|
| HIGH | LOW  | Forward | HIGH | LOW  | Forward |
| LOW  | HIGH | Reverse | LOW  | HIGH | Reverse |
| LOW  | LOW  | Stop    | LOW  | LOW  | Stop |

## Notes
- ENA and ENB must be HIGH for motors to run — use jumper caps to bridge them to 5V
- Wire colors match mapping.yml: blue=GPIO17, white=GPIO27, green=GPIO22, yellow=GPIO23
