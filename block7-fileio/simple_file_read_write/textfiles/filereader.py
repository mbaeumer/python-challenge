#!/usr/bin/python

print("Demo of simple file reading")
print("")

try:
  file = open("persons.txt", "r")
  for line in file:
    print(line)
  file.close()
except FileNotFoundError as e:
  print("The file does not exist!")
