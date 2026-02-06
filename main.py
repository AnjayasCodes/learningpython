import time

desired_time = int(input("Enter the time in sec"))

for x in range(desired_time, 0, -1):
    sec = x % 60
    minute = (x//60) % 60
    hour = x//3600
    print(f"{hour:02d}:{minute:02d}:{sec:02d}")
    time.sleep(1)
