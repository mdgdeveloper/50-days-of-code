# Create a function called alarm that sets an alarm clock for the
# user. The function should ask the user to enter time they want
# the alarm to go off. The user should enter the hour and
# minute. The function should then print out the time when the
# alarm will go off. When its alarm time, the code should let off a
# sound. Use the winsound module for sound.

import winsound
from datetime import datetime
import time


def alarm():
    print("=== Alarm Clock v1 ===")
    timeInput = input("Introduce the hour and minutes in HH:MM format: ")

    alarmOn = True

    while(alarmOn):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        if(current_time == timeInput):
            alarmOn = False
        time.sleep(1)

    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)


# Test
alarm()
