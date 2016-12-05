#!/usr/bin/python
import time

print("Some time and date stuff")
print("------------------------")
now = time.asctime(time.localtime(time.time()))
print("the current time: " + now)
