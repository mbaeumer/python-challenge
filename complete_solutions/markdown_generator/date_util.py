#!/usr/bin/python
import datetime

class DateHandler:
  def __init__(self):
    self.completeDateString = ""
    self.offset = "+0100"

  def constructDateString(self):
    result = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    self.completeDateString = result + " " + self.offset 
    return self.completeDateString

