#!/usr/bin/python
print("Demo of if statements")
print("")
try:
  number = int(input("Please enter a number: "))
  if number > 0:
    print("You  enered a positive number.")
  elif number < 0:
    print("You entered a negative number.")
  else:
    print("You entered zero.")
except ValueError as ex:
  print("Enter a valid number")

