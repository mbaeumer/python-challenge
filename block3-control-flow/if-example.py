#!/usr/bin/python
print("Demo of if statements")
print("")

def demo_if_else():
  try:
    number = int(input("Please enter a number: "))
    if number > 0:
      print("The number is larger than zero.")
    else:
      print("The number is not larger than zero.")
  except ValuError as ex:
    print("Enter a valid number")  

def demo_if_elif():
  try:
    number = int(input("Please enter a number: "))
    if number > 0:
      print("You entered a positive number.")
    elif number < 0:
      print("You entered a negative number.")
    else:
      print("You entered zero.")
  except ValueError as ex:
    print("Enter a valid number")

def demo_ternary():
  try:
    message=""
    number = int(input("Please enter a number: "))
    message="The number is larger than zero." if number > 0 else "The number is not larger than zero."
    print(message) 
  except ValueError as ex:
    print("Enter a valid number")


if __name__ == '__main__':
  demo_if_else()
  demo_if_elif()
  demo_ternary()
