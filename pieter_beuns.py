import communicate
import time
import datetime

buffer = ""
while True:

    a = datetime.datetime.now()
    today = datetime.datetime.today()
    goal = datetime.datetime.combine(today, datetime.time(hour=20))

    final_time = goal - a
    final_string = str(final_time.seconds // 3600) + " hours and " + str((final_time.seconds // 60 % 60)) + " minutes until Cantus"

    if buffer != final_string:
        communicate.write("daan", "pieter", final_string)
        print(final_string)
    final_string = buffer
    time.sleep(60)
