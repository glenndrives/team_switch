****
## Team response to cst 1:

Event Status:

|   |          EVENT              |   # |   |ACTION |   | R.T. STATE|   |LATCHED STATE|
|---|-----------------------------|-----|---|-------|---|-----------|---|-------------|
|   |T1 Mux Missing               |  N01|   | NONE  |   | NOT ACTIVE|   | NOT ACTIVE  |
|   |T1 Mux Init Failure          |  N02|   | NONE  |   | NOT ACTIVE|   | NOT ACTIVE  |
|   |T1 Loss of Sync              |  N05|   | NONE  |   | NOT ACTIVE|   | ACTIVE      |
|   |T1 Loss of Signal            |  N06|   | NONE  |   | NOT ACTIVE|   | ACTIVE      |
|   |T1 AIS On                    |  N11|   | NONE  |   | NOT ACTIVE|   | NOT ACTIVE  |
|   |T1 Loss of Frame Alignment   |  N19|   | NONE  |   | NOT ACTIVE|   | ACTIVE      |
|   |T1-D Loss of Signal          |  N20|   | NONE  |   | ACTIVE    |   | ACTIVE      |
|   |T1-D AIS On                  |  N21|   | NONE  |   | NOT ACTIVE|   | ACTIVE      |
|   |T1-D Loss of Frame Alignment |  N22|   | NONE  |   | ACTIVE    |   | ACTIVE      |
|---|-----------------------------|-----|---|-------|---|-----------|---|-------------|
| 1 | 33                          | 3   | 4 |    4  | 5 |  10       | 4 | 10          |

## VCL response to alarms_sum?

 SYSTEM ALARMS SUMMARY:
 
|    |       |         |        |
|----|-------|---------|--------|
|T1 |PORT-01|Main   ->|NO_ALARM|  
|T1 |PORT-01|Standby->|ALARM_ON**|
|T1 |PORT-01|Eqpmt  ->|NO_ALARM|  
|T1 |PORT-02|->ALARMS |DISABLED|
|T1 |PORT-03|->ALARMS |DISABLED|
|T1 |PORT-04|->ALARMS |DISABLED|
|T1 |PORT-05|->ALARMS |DISABLED|
|T1 |PORT-06|->ALARMS |DISABLED|
|T1 |PORT-07|->ALARMS |DISABLED|
|T1 |PORT-08|->ALARMS |DISABLED|
|---|-------|---------|--------|
| 3 |   7   |    9    |    8   |

+   the asterisks for ALARM_ON are truncated off

## 99-usb-serial.rules

>Had to add /etc/udev/rules.d/99-usb-serial.rules to get around serial adapters changing /dev/ file naming 
>at boot time. 

## VCL alarm Contact
>| Screw terminals on the back. Use NO | NO Pi Pin 36 (GPIO 16) | COM Pi Pin 30 (Ground) |

## Team Alarm Relays
> T1 Loss of Sync on relay A
>
>| Alarm Relay A common Pin 9 | Pi Pin 34 (Ground)|
>
>| Alarm Relay A NO Pin 22 | Pi Pin 38 (GPIO 20) |

> T1 Loss of Signal on relay B
>
>| Alarm Relay B common Pin 23 | Pi Pin 39 (Ground) |
>
>| Alarm Relay B NO Pin 11 | Pi Pin 40 (GPIO 21) |

## Python Pull up-down
>You enable these internal pull-ups/pull-downs at the time of setting up the port for input or output, by adding an extra, optional, argument to the GPIO.setup() function call.
>
>We’re using pull-down, so it’s pull_up_down=GPIO.PUD_DOWN. If you want/need pull-up you can change the PUD_DOWN for PUD_UP. (It depends on how you’ve wired your circuit.)
>
>GPIO.setup(port_or_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)




