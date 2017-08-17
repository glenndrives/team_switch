#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import serial
import pandas as pd

team = serial.Serial("/dev/ttyUSB0", 38400, timeout=1)
vlc = serial.Serial("/dev/ttyUSB1", 9600, timeout=1)

vclPort01Main = ""
vclPort01Standby = ""
vlcPort01Eqpmt = ""
teamN05 = ""
teamN06 = ""

def slices(s, *args):
    position = 0
    for length in args:
        yield s[position:position + length]
        position += length

vlc.write('alarms_sum?\n')

while True:
    c = vlc.readline()
    if len(c) ==0:
        break
    if "01Main" in c:
        vclPort01Main = c
    if "01Standby" in c:
        vclPort01Standby = c
    if "01Eqpmt" in c:
        vclPort01Eqpmt = c

team.write('cst 1\n')

while True:
    c = team.readline()
    if len(c) == 0:
        break
    if "N05" in c:
        teamN05 = c
    if "N06" in c:
        teamN06 = c

print(list(slices(vclPort01Main, 3, 7, 9, 10))[3])
print(list(slices(vclPort01Standby, 3, 7, 9, 10))[3])
print(vclPort01Eqpmt)

print(list(slices(teamN05, 1, 33, 3, 4, 4, 5, 10, 4, 10))[6])
print(list(slices(teamN05, 1, 33, 3, 4, 4, 5, 10, 4, 10))[6])
