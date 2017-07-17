#!/usr/bin/python
import re

def main():
  print_title()
  strings = create_string_list()
  for s in strings:
    print("String to bet tested: %s" % (s))
    print(check_static_search(s))
    print(check_static_match(s))
    print(check_static_findall(s))

def print_title():
  print("Demo of dynamic regex usage")
  print("")

def create_string_list():
  strings = []
  strings.append('test2')
  strings.append('1est12')
  strings.append('pas5w0rd1')
  return strings

def get_numbers():
  finished = False
  numbers = 0
  while not finished:
    try:
      numbers = int("How many numbers you want to check for? ")
      if numbers <= 0:
        raise ValueError
      finished = True
    except ValueError:
      print("ERROR: Please enter a valid number!")
  return numbers

def check_static_search(teststring):
  return re.search(r'\d{2}', teststring)

def check_static_match(teststring):
  return re.match(r'[\w\d{2}]', teststring)

def check_static_findall(teststring):
  return re.findall(r'[\d]', teststring)


if __name__ == '__main__':
  main()
