# Raspberry Pi Greeter
Make your Raspberry Pi speak a greeting when you arrive.
It works by routinely checking bluetooth for any registered devices, then speaks a greeting or farewell when the device is rediscovered or lost.

## Requirements
You will need bluez to handle bluetooth and gnustep-gui-runtime to run text-to-speech.
Use the below commands to install them.

```bash
sudo apt -y install bluez python-bluez
sudo apt -y install gnustep-gui-runtime
```

## Usage
1. Clone the repo and cd in with `git clone https://github.com/AlexLamson/rpi-greeter && cd rpi-greeter`
2. Put your device into bluetooth discoverable mode
3. Run `python add_user.py` and follow the directions to add your device
4. Run the greeter in the background with `python greeter.py &`
