#Luke Murdock, Time Stamp Creator
import datetime as dt

def stamp():
    time = str(dt.datetime.now())
    return time[:-7]