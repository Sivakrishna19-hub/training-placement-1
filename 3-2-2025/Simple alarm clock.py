import time
import winsound

def alarm_clock(seconds):
    print(f"Alarm set for {seconds} seconds.")
    time.sleep(seconds)
    winsound.Beep(1000, 1000)
    print("Time's up!")

alarm_time = int(input("Enter alarm time in seconds: "))
alarm_clock(alarm_time)
