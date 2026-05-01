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

## SSH Access
```
ssh driver@rc-car.local
```
