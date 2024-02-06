# https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203

""" 
    * Module Install
    * -> pip install playsound
    
    -> playsound : এইটা ব্যবহার করে সাউন্ড প্লে করা হয়ে থাকে
    -> time : এই মডিউল দিয়ে টাইমের কাজ করা হয় 
"""

from playsound import playsound
import time

CLEAR = "\033[2J"  # -> Use for Clear Step by Step
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        second_left = time_left % 60

        print(
            f"{CLEAR_AND_RETURN}Alarm will sound In : {minutes_left:02d}:{second_left:02d}")
    playsound("Alarm.mp3")


minutes = int(input("How Many Minutes to wait : "))
seconds = int(input("How Many Seconds to wait : "))
total_seconds = (minutes*60)+seconds
alarm(total_seconds)

# playsound("../04_Mini-Project/Alarm.mp3")
