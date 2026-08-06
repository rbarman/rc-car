```mermaid
graph TD
    subgraph Pi [Raspberry Pi 4]
        FiveV[5V - Pin 4]
        PiGND[GND - Pin 6]
        GPIO24[GPIO 24 - Pin 18]
    end

    FiveV -->|"Purple wire"| DCplus
    PiGND -->|"Orange wire"| DCminus
    GPIO24 -->|"Brown wire"| IN

    subgraph Relay [5V Relay Module]
        DCplus[DC+]
        DCminus[DC-]
        IN[IN]
        COM[COM - not wired yet]
        NO[NO - not wired yet]
        NC[NC - not wired yet]
    end

    linkStyle 0 stroke:#a855f7,stroke-width:3px
    linkStyle 1 stroke:#f97316,stroke-width:3px
    linkStyle 2 stroke:#78350f,stroke-width:3px
```

## Notes
- This step only wires the relay's **control side** (`DC+`, `DC-`, `IN`) to the Pi — nothing on the switching side (`NO`/`COM`/`NC`) is connected yet, so no pump or battery is involved
- This relay board (Songle SRD-05VDC-SL-C) has no physical trigger-level jumper despite the "high/low level trigger" silkscreen text — that's just generic printed spec text, not an adjustable part. Trigger polarity (active-high vs. active-low) was confirmed empirically by running `relay_test.py` and watching `LED1` / listening for the click
- Ground here is just the Pi's own GND pin — no need to touch the motor battery/shared ground rail until the pump is introduced in step 2

## Wire colors used
| Wire color | Pi pin | Relay terminal |
|---|---|---|
| Purple | Pin 4 (5V) | `DC+` |
| Orange | Pin 6 (GND) | `DC-` |
| Brown | Pin 18 (GPIO24) | `IN` |
