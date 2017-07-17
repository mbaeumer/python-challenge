#!/usr/bin/python
import re

def do_match(s):
  print("Example of re.match")
  print("The string:  %s " % (s))
  if re.match(r'^http://', s):
    print('There is a match')
  else:
    print('There is no match')


def do_search(s):
  print("Example of re.search")
  print("The string:  %s " % (s))
  if re.search(r'^http://', s):
    print('There is a match')
  else:
    print('There is no match')

def main():
  print("Some examples of regex")
  do_match('http://someurl.com')
  do_match('someurl.com')
  do_search('http://someurl.com')
  do_search('someurl.com')

# main
if __name__ == '__main__':
  main()
