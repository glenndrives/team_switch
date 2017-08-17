# team_switch
## Project with a Raspberry Pi to reset the Team MUX if it locks up after a T1 error

>This project is utilizing a Raspberry Pi ver.3 with two USB to RS232 adapters to interface with a TEAM T1 MUX
>and a VCL-SafeComm T1 switch at the transmitter location.

>The Raspberry Pi will either poll the TEAM unit periodically for alarms or monitor an alarm contact closure for
>active alarms.

>When an alarm is detected the Pi will decide if a reboot of the TEAM unit is required. Basically if the TEAM T1
>iterface is in alarm and either or both VCL T1 paths are good the TEAM will be reset. If both VCL paths are in
>alarm there is no need to reset the TEAM as there is not a connection to the studio.
