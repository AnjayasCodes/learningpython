import time


def count(start=0, end):
    for x in range(start, end+1, 1):
        print(x)
        time.sleep(1)


count(1, 30)
