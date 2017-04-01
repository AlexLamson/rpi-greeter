#!/usr/bin/python

import bluetooth
import os.path


users_path = 'users.txt'


# Get the current list of users
users = []
if os.path.isfile(users_path):
    with open(users_path, 'r') as f:
        for user_str in f.read().split('\n'):
            if len(user_str) > 0:
                addr = user_str[:17]
                name = user_str[18:]
                users.append( (addr, name) )

# Look for discoverable devices
print("Scanning for nearby bluetooth devices...")
nearby_devices = bluetooth.discover_devices(lookup_names = True)

if len(nearby_devices) == 0:
    print("No bluetooth devices found. Is your device in discoverable mode?")
    exit()

# Let the user choose their device
for i, (addr, name) in enumerate(nearby_devices):
    print("[{}] {} {}".format(i, addr, name))

num = raw_input("Enter the number of your device (or type anything else to quit)\n")

if not num.isdigit():
    exit()
elif num.isdigit() and not (0 <= int(num) < len(nearby_devices)):
    print("Digit not in valid range")
else:
    addr, name = nearby_devices[int(num)]

    # If the device is already in the list, let them rename it
    device_index = -1
    if addr in [x[0] for x in users]:
        device_index = [x[0] for x in users].index(addr)
    if device_index > -1:
        maybe_name = raw_input("Device already registered. Enter a new name for this device (or press enter to keep '{}')\n".format(name))
        users.pop(device_index)
    else:
        maybe_name = raw_input("Enter a name for this device (or press enter to use '{}')\n".format(name))

    if maybe_name != '':
        name = maybe_name

    users.append( (addr, name) )

    with open(users_path, "w") as users_file:
        users_string = "\n".join(["{} {}".format(addr, name) for addr, name in users])
        users_file.write( users_string )
    print("Successfully added '{}'".format(name))

