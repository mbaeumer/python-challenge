#!/usr/bin/python

def generate_heading(level, text):
  result = ""
  i = 0
  while i < level:
    result = result + "#"
    i = i + 1
  result = result + " " + text
  return result 

def generate_bullet_list(list):
  result = "\n"
  for item in list:
    result = result + "* " + item + "\n"
  result = result + "\n"
  return result
 

