#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


import sys
import serial
import RPi.GPIO as GPIO  # Import Python GPIO module

GPIO.setmode(GPIO.BCM)  # Set board mode to Broadcom

team = serial.Serial("/dev/ttyUSB0", 38400, timeout=1)  # Start serial port for TEAM unit
vcl = serial.Serial("/dev/ttyUSB1", 9600, timeout=1)  # Start serial port for VCL

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

vcl.write('alarms_sum?\n')  # Get alarms from VCL

# Loop through VLC response and get alarm conditions

while True:
    c = vcl.readline()
    if len(c) ==0:
        break
    if "01Main" in c:
        vclPort01Main = list(slices(c, 3, 7, 9, 8))[3]  # captures only the alarm condition
    if "01Standby" in c:
        vclPort01Standby = list(slices(c, 3, 7, 9, 8))[3]  # captures only the alarm condition
    if "01Eqpmt" in c:
        vclPort01Eqpmt = list(slices(c, 3, 7, 9, 8))[3]  # captures only the alarm condition

team.write('cst 1\n')  # Get alarms from TEAM

# Loop through TEAM response and get alarm conditions

while True:
    c = team.readline()
    if len(c) == 0:
        break
    if "N05" in c:
        teamN05 = (list(slices(c, 1, 33, 3, 4, 4, 5, 10, 4, 10))[6])  # captures only the alarm condition
    if "N06" in c:
        teamN06 = (list(slices(c, 1, 33, 3, 4, 4, 5, 10, 4, 10))[6])  # captures only the alarm condition

# Print out alarm responses for troubleshooting

print("VCL Port 01 Main = " + str(vclPort01Main))
print("VCL Port 01 Standby = " + str(vclPort01Standby))
print("VCL Port 01 Equipment = " + str(vclPort01Eqpmt))

print("Team N05 Loss of Sync = " + str(teamN05))
print("Team N06 Loss of Signal = " + str(teamN06))
