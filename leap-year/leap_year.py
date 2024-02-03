#!/usr/bin/python

def is_leap_year(year):
  if (year % 400 == 0 and year % 100 == 0) or (year % 4 == 0 and year % 100 != 0):
      return True
  return False


if __name__ == '__main__':
  is_leap_year(2000)