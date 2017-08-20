#!/usr/bin/python
from datetime import datetime
from dateutil.relativedelta import relativedelta

def main():
  print("Demo of date operations")
  today = datetime.now()
  date = datetime.strptime("2017-07-01", "%Y-%m-%d")
  date2 = datetime.strptime("2017-06-30", "%Y-%m-%d")
  if today > date > date2:
    print("Today after...")
  else:
    print("Today before...")
 

if __name__ == '__main__':
  main()
