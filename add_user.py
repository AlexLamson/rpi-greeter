#!/usr/bin/python

import bluetooth

print("Scanning for bluetooth devices in discoverable mode...")
nearby_devices = bluetooth.discover_devices(lookup_names = True)

for i, (addr, name) in enumerate(nearby_devices):
    print("[{}] {} {}".format(i, addr, name))

num = raw_input("Enter the number of your device (or type anything else to quit)\n")

if num.isdigit() and 0 <= int(num) < len(nearby_devices):
    addr, name = nearby_devices[int(num)]

    maybe_name = raw_input("Enter a name for this device (or press enter to use '{}')\n".format(name))
    if maybe_name != '':
        name = maybe_name

    with open("users.txt", "a") as users_file:
        users_file.write("{} {}\n".format(addr, name))
    print("Successfully added '{}'".format(name))

else:
    exit()
