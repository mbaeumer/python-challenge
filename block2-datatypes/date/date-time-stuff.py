#!/usr/bin/python
import time
import datetime

print("Some time and date stuff")
print("------------------------")
now = time.asctime(time.localtime(time.time()))
print("the current time using the time module: " + now)

print("Creating a date only using datetime")
date = datetime.datetime.strptime("2017-07-01", "%Y-%m-%d")
print("The date in the format Y-m-d: " + date.strftime("%Y-%m-%d"))
print("The date in the format Y-m-d H:m: " + date.strftime("%Y-%m-%d %H:%M"))

print("Creating a date with time using datetime")
date = datetime.datetime.strptime("2017-07-01 15:34", "%Y-%m-%d %H:%M")
print(date.strftime("%Y-%m-%d %H:%M"))

print("Adding some time to an existing date")
date1 = datetime.datetime.strptime("2017-07-01 15:34", "%Y-%m-%d %H:%M")
date2 = date1 + datetime.timedelta(days=1)
print("date1: " + date1.strftime("%Y-%m-%d %H:%M"))
print("date2: " + date2.strftime("%Y-%m-%d %H:%M"))

print("Calculating the difference between two dates")
date2 = datetime.datetime.strptime("2017-07-02 16:35", "%Y-%m-%d %H:%M")
print("all: ", date2 - date1)
print("days: ", (date2 - date1).days)
print("seconds: ", (date2 - date1).seconds)
print("microseconds: ", (date2 - date1).microseconds)

