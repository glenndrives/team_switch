#!/usr/bin/env python
# -*- coding utf-8 -*-

import RPi.GPIO as GPIO  # Import Python GPIO
GPIO.setmode(GPIO.BCM)  # Set GPIO mode to Broadcom for pinout

# set inputs for alarm relays
team_relay_a = 20
team_relay_b = 21
vcl_relay = 16

# configure inputs
GPIO.setup(team_relay_a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(team_relay_b, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(vcl_relay, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# print status of inputs
print(GPIO.input(team_relay_a))
print(GPIO.input(team_relay_b))
print(GPIO.input(vcl_relay))

GPIO.cleanup()
