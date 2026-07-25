# Backlog

Items to revisit or consider for future milestones.

| # | Item | Notes |
|---|------|-------|
| 1 | Pivot to 2 motor drivers | Currently using 1 L298N for all 4 motors. If current draw is insufficient, split into one driver per side. |
| 2 | Servo steering | Replace tank steering with a servo-controlled front axle for more realistic driving feel. Requires a different chassis with pivoting front wheels and a servo motor. |
| 3 | Off-WiFi remote control | Current web controller requires phone + Pi on the same WiFi network. See options below for removing that dependency. |

### Off-WiFi remote control options (for item 3)

The web controller (`controller/app.py`) only works when the phone and Pi share a WiFi network. Options considered, roughly cheapest/lowest-effort first:

- **WiFi AP mode on the Pi** — turn the Pi into its own hotspot (`hostapd` + `dnsmasq`) so the phone connects directly to it. No new hardware, reuses the existing Flask UI unchanged. Range ~20-30m, phone has to manually switch WiFi networks.
- **Bluetooth gamepad** — pair a BT gamepad (e.g. 8BitDo, ~$15-25) to the Pi's onboard Bluetooth, read input with `pygame`/`evdev`, map sticks to motor commands. No soldering, no WiFi dependency. Don't currently own a gamepad.
- **Classic Bluetooth (RFCOMM/SPP) or BLE** — Pi listens for a phone connection over Bluetooth instead of WiFi. Classic BT is Android-only in practice (iOS restricts raw RFCOMM); BLE works on both but needs either a generic BLE tool app or a custom mobile app — no free "nice UI" like the web controller.
- **Hobby RC transmitter + receiver** (e.g. FlySky FS-i6X, ~$35-50) — real long-range 2.4GHz radio gear. Receiver outputs PWM/PPM per channel; decode pulse widths on the Pi via GPIO + `pigpio`, with voltage-divider level shifting (receiver outputs 5V, Pi GPIO is 3.3V). Long range (100m+), proper transmitter ergonomics, no firmware to write.
- **Build a custom NRF24L01 remote** — handheld transmitter (Arduino Nano/ESP32 + joysticks + NRF24L01, ~$10-15 in parts) talks to a matching NRF24L01 on the Pi's SPI pins (GPIO 9/10/11 + CE0/CE1, no conflict with existing motor GPIOs 17/27/22/23). Cheapest in parts but the most build effort — soldering, Arduino firmware, and Pi-side packet decoding.
- **Cellular + Tailscale VPN** — keeps the existing web controller reachable from anywhere with internet by tunneling back to the home network. Doesn't remove the "needs a network" constraint, just extends which network counts — best for remote access, not for local WiFi-free driving.

Leaning toward WiFi AP mode as the highest-value/lowest-effort next step, with the hobby RC transmitter as the better long-term "real remote" option if going the buy-a-controller route.
