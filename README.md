# RC Car

A 4-wheel RC car controlled via a web browser, built with a Raspberry Pi 4 and L298N motor driver.

<video src="milestones/6_controller/test_drive.mp4" controls width="600"></video>

## Pi Setup

- **Model:** Raspberry Pi 4B
- **OS:** Raspberry Pi OS Lite
- **Hostname:** `rc-car`
- **User:** `driver`

## Starting the Car

1. Connect and turn on the **motor battery pack** to the L298N (+12V terminal)
2. Connect the **phone charger** to the Raspberry Pi (USB-C)
3. Wait ~30 seconds for the Pi to boot and the web controller to start automatically

## Controlling the Car

1. Connect your phone or laptop to the **same WiFi network** as the Pi
2. Open a browser and go to:
   ```
   http://rc-car.local:5000
   ```
3. Use the on-screen buttons to drive. Hold a button to move, release to stop.

## Troubleshooting

**Can't connect to rc-car.local:5000**
- Make sure your device is on the same WiFi as the Pi
- SSH into the Pi and check the service: `sudo systemctl status rc-car`
- Restart the service: `sudo systemctl restart rc-car`

**Motors not responding**
- Check the motor battery pack is on and connected to the +12V terminal on the L298N
- Check the Pi is powered (should have a solid red LED)
- Verify battery pack polarity: **red wire → +12V terminal**, **black wire → GND terminal** on the L298N (not both to +12V — that shorts the battery pack across its own terminals)
- Quick power checks: the **L298N has an onboard red power LED** that lights up when it's properly wired to the battery pack — if it's dark, recheck the battery connection/polarity before going further. The **Pi shows a solid red LED** once it has power (a blinking/no green LED separately indicates SD card activity/boot issues, but red = power is present)

**Validating motor wiring (which pin drives which wheel)**
1. Prop the car up so all wheels spin freely — don't let it drive off the table
2. SSH in and stop the web controller first, since it holds the same GPIO pins: `sudo systemctl stop rc-car`
3. Run the pin tester: `python3 pin_test.py`
4. Activate pins `1`-`4` one at a time and confirm:
   - `1`/`2` (GPIO 17/27) spin **both left motors** (front-left + back-left), opposite directions from each other
   - `3`/`4` (GPIO 22/23) spin **both right motors**, opposite directions from each other
5. `0` stops all pins, `q` quits
6. Restart the web controller when done: `sudo systemctl start rc-car`

**`lgpio.error: 'GPIO busy'` when running a test script**
- The `rc-car` systemd service is already running and holds the motor GPIO pins
- Stop it first: `sudo systemctl stop rc-car`, then re-run the script
- Restart it afterward: `sudo systemctl start rc-car`

## SSH Access
```
ssh driver@rc-car.local
```
