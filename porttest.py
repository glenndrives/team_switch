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
        vclPort01Main = list(slices(c, 3, 7, 9, 8))[3]
    if "01Standby" in c:
        vclPort01Standby = list(slices(c, 3, 7, 9, 8))[3]
    if "01Eqpmt" in c:
        vclPort01Eqpmt = list(slices(c, 3, 7, 9, 8))[3]

team.write('cst 1\n')

while True:
    c = team.readline()
    if len(c) == 0:
        break
    if "N05" in c:
        teamN05 = (list(slices(c, 1, 33, 3, 4, 4, 5, 10, 4, 10))[6])
    if "N06" in c:
        teamN06 = (list(slices(c, 1, 33, 3, 4, 4, 5, 10, 4, 10))[6])

print(vclPort01Main)
print(vclPort01Standby)
print(vclPort01Eqpmt)

print(teamN05)
print(teamN06)
