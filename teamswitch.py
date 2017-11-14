#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' IMPORTANT READ!!!
    This code only works under Python 3.4.2 and up.
'''

# (C) Copyright 2017 Glenn Hickman <glennh@gjjtjc.com>
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

# built in modules
import sys
import serial  # Import Python Serial module
from time import sleep

# RPi specific modules
import RPi.GPIO as GPIO  # Import Python GPIO module

# Our modules
import sendemail  # function to send an email sendemail.sendemail("msg", "from", "to")

#The next two lines set up the relay board for use
from mcp23008 import mcp23008  # Import the MCP23008 library from ncd.io (https://github.com/ncd-io/MCP23008) to control the relays
import smbus  # smbus to interact with I2C bus

#The following lines setup the mcp23008 library for the relay board
bus = smbus.SMBus(1)  # Get I2C bus, bus 1
gpio_output_map = {0,1}  # defines which GPIOs of the MCP23008 are outputs for the relays. All others are default inputs
kwargs = {'address': 0x20, 'gpio)out_output_map': gpio_output_map}  # kwargs is a se that the device address and output map to be passed to the objec for initialization
mcp23008 = mcp23008(bus, kwargs)  # pass the bus and kwargs to the mcp23008 object

GPIO.setmode(GPIO.BCM)  # Set board mode to Broadcom

# We have to determine which serial port has which device as the USB adapters can
# change device files.

team = serial.Serial("/dev/mttyUSB0", 38400, timeout=1)  # Start serial port for TEAM unit
vcl = serial.Serial("/dev/mttyUSB1", 9600, timeout=1)  # Start serial port for VCL

vclPort01Main = ""
vclPort01Standby = ""
vclPort01Eqpmt = ""
teamN05 = ""
teamN06 = ""

# Borrowed function to parse serial data from TEAM and VCL
# https://stackoverflow.com/questions/4914008/how-to-efficiently-parse-fixed-width-files

def slices(s, *args):
    position = 0
    for length in args:
        yield s[position:position + length]
        position += length

vcl.write('alarms_sum?\n'.encode())  # Get alarms from VCL

# Loop through VLC response and get alarm conditions

while True:
    c = vcl.readline()
    if len(c) ==0:
        break
    if "01Main" in str(c):
        vclPort01Main = list(slices(c, 3, 7, 9, 8))[3]  # captures only the alarm condition
    if "01Standby" in str(c):
        vclPort01Standby = list(slices(c, 3, 7, 9, 8))[3]  # captures only the alarm condition
    if "01Eqpmt" in str(c):
        vclPort01Eqpmt = list(slices(c, 3, 7, 9, 8))[3]  # captures only the alarm condition

team.write('cst 1\n'.encode())  # Get alarms from TEAM

# Loop through TEAM response and get alarm conditions

while True:
    c = team.readline()
    if len(c) == 0:
        break
    if "N05" in str(c):
        teamN05 = (list(slices(c, 1, 33, 3, 4, 4, 5, 10, 4, 10))[6])  # captures only the alarm condition
    if "N06" in str(c):
        teamN06 = (list(slices(c, 1, 33, 3, 4, 4, 5, 10, 4, 10))[6])  # captures only the alarm condition

# Print out alarm responses for troubleshooting
print("VCL and TEAM Alarms\n")
print("VCL Port 01 Main = " + str(vclPort01Main))
print("VCL Port 01 Standby = " + str(vclPort01Standby))
print("VCL Port 01 Equipment = " + str(vclPort01Eqpmt))

print("Team N05 Loss of Sync = " + str(teamN05))
print("Team N06 Loss of Signal = " + str(teamN06))
print("\nRelay Board Status\n")
print("GPIO Status = " + str(mcp23008.get_all_gpio_status()))

msg = "\nVCL and TEAM Alarms\n\n"
msg += "VCL Port 01 Main = " + str(vclPort01Main) + "\n"
msg += "VCL Port 01 Standby = " + str(vclPort01Standby) + "\n"
msg += "VCL Port 01 Equipment = " + str(vclPort01Eqpmt) + "\n"
msg += "Team N05 Loss of Sync = " + str(teamN05) + "\n"
msg += "Team N06 Loss of Signal = " + str(teamN06) + "\n\n"
msg += "Relay Board Status\n\n"
msg += "GPIO Status = " + str(mcp23008.get_all_gpio_status())
print(msg)

sendemail.sendemail(msg, "teamswitch@whro.org", "glennh@whro.org")

