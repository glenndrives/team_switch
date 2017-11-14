#!/usr/bin/env python
# -*- coding utf-8 -*-

import time  # need to be able to sleep
import sendemail  # function to send emails
import RPi.GPIO as GPIO  # Import Python GPIO

GPIO.setmode(GPIO.BCM)  # Set GPIO mode to Broadcom for pinout

'''
The interrupt handler for the Pi is buggy and triggers on any transition
no matter how you set the type of detection. To fix this we have to test the
state of the input to see if it is high or low. To do this the lines:

time.sleep(0.005)
    if GPIO.input(team_relay_a) == 0:

were added. We sleep for a short while then check the state of the input to
determine if we need to react. In this case we are looking for an active low.

Used code from https://www.raspberrypi.org/forums/viewtopic.php?t=134394

'''
def handle(pin):
    time.sleep(0.005)
    if GPIO.input(team_relay_a) == 0:
        sendemail.sendemail("Detected Alarm " + str(pin), "teamswitch@whro.org", "glennh@whro.org")
        print(str(pin))



# set inputs for alarm relays
team_relay_a = 20
team_relay_b = 21
vcl_relay = 16

# configure inputs
GPIO.setup(team_relay_a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(team_relay_b, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(vcl_relay, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(team_relay_a, GPIO.RISING, callback=handle, bouncetime=1000)
GPIO.add_event_detect(team_relay_b, GPIO.RISING, callback=handle, bouncetime=1000)

try:
    while True:
        time.sleep(.1)

except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
