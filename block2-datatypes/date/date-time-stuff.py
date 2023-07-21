#!/usr/bin/python
import time

import datetime
from dateutil.relativedelta import relativedelta

def create_date_with_time():
  print("Creating a date using time")
  now = time.asctime(time.localtime(time.time()))
  print("the current time using the time module: " + now)

def create_date_with_datetime():
  print("Creating a date without time using datetime")
  date = datetime.datetime.strptime("2017-07-01", "%Y-%m-%d")
  print("The date in the format Y-m-d: " + date.strftime("%Y-%m-%d"))
  print("The date in the format Y-m-d H:m: " + date.strftime("%Y-%m-%d %H:%M"))

  print("Trying to create a date with a wrong string")
  try:
    date = datetime.datetime.strptime("2017-07-ab", "%Y-%m-%d")
  except ValueError:
    print("ERROR: The given string is not suitable for a date!")

  print("Creating a date with time using datetime")
  date = datetime.datetime.strptime("2017-07-01 15:34", "%Y-%m-%d %H:%M")
  print(date.strftime("%Y-%m-%d %H:%M"))

def time_arithmetic():
  print("Adding some time to an existing date")
  date1 = datetime.datetime.strptime("2017-07-01 15:34", "%Y-%m-%d %H:%M")
  one_day = date1 + datetime.timedelta(days=1)
  one_week = date1 + datetime.timedelta(weeks=1)
  one_month = date1 + relativedelta(months=+1)
  print("date1: " + date1.strftime("%Y-%m-%d %H:%M"))
  print("date2 (one day): " + one_day.strftime("%Y-%m-%d %H:%M"))
  print("date3 (one week): " + one_week.strftime("%Y-%m-%d %H:%M"))
  print("date4 (one month): " + one_month.strftime("%Y-%m-%d %H:%M"))

def calculate_time_difference():
  print("Calculating the difference between two dates")
  date1 = datetime.datetime.strptime("2017-07-01 15:34", "%Y-%m-%d %H:%M")
  date2 = datetime.datetime.strptime("2017-07-02 16:35", "%Y-%m-%d %H:%M")
  print("all: ", date2 - date1)
  print("days: ", (date2 - date1).days)
  print("seconds: ", (date2 - date1).seconds)
  print("microseconds: ", (date2 - date1).microseconds)

def get_date_details():
  date = datetime.date.today()
  print("year: %d" % (date.year))
  print("month: %d" % (date.month))
  print("day: %d" % (date.day))

def get_datetime_partials():
  date = datetime.datetime.now()
  print("year: %d" % (date.year))
  print("month: %d" % (date.month))
  print("day: %d" % (date.day))
  print("hour: %d" % (date.hour))
  print("minute: %d" % (date.minute))
  print("second: %d" % (date.second))
  print("weekday: %d" % (date.weekday()))

def set_datetime_year(year_input):
  date = datetime.datetime.now()
  print("year before: %d" % (date.year))
  # NOTE: date/datetime are immutable. Use date.replace to change parts of a date
  date = date.replace(year = year_input)
  print("year after: %d" % (date.year))

def show_type_of_date_and_datetime():
  date1 = datetime.datetime.strptime("2017-07-01 15:34", "%Y-%m-%d %H:%M")
  date2 = datetime.datetime.strptime("2017-07-02", "%Y-%m-%d")
  print(type(date1))
  print(type(date2))



if __name__ == '__main__':
  print("Some time and date stuff")
  print("------------------------")
  create_date_with_time()
  create_date_with_datetime()
  time_arithmetic()
  calculate_time_difference()
  get_datetime_partials()
  get_date_details()
  set_datetime_year(2032)
  show_type_of_date_and_datetime()

