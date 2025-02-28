#Luke Murdock, Time Stamp Creator
import datetime as dt

def stamp(): # Uses datetime to find the exact time when the text stamp was added and then returns it in the correct format
    time = str(dt.datetime.now())
    return time[:-7]
