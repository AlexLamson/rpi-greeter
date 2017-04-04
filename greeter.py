#!/usr/bin/python

import bluetooth
import time
import os


users_path = 'users.txt'
timeout = 3
sleep_time = 5


# Get the current list of users
users = []
if os.path.isfile(users_path):
    with open(users_path, 'r') as f:
        for user_str in f.read().split('\n'):
            if len(user_str) > 0:
                addr = user_str[:17]
                name = user_str[18:]
                users.append( (addr, name) )
if len(users) == 0:
    print("No users found")
    exit()

# Initialize the state of all the users
def check_visible(addr):
    return (bluetooth.lookup_name(addr, timeout=timeout) != None)

visible_users = [check_visible(addr) for addr, name in users]
print("States initialized")


# If a user changes state, greet them / wish them goodbye
while True:
    time.sleep(sleep_time)
    
    for i, (addr, name) in enumerate(users):
        is_visible = check_visible(addr)
        was_visible = visible_users[i]

        if is_visible and not was_visible and check_visible(addr):
            print("Welcome back {}!".format(name))
            os.system('say "Welcome back {}!"'.format(name))

        elif not is_visible and was_visible and not check_visible(addr):
            print("Goodbye {}!".format(name))
            os.system('say "Goodbye {}!"'.format(name))

        visible_users[i] = is_visible

        # prevent error where multiple users receive one user's state change
        time.sleep(0.1)

