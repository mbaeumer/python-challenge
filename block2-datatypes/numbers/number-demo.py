#!/usr/bin/python
from decimal import Decimal
from decimal import DecimalException
import random

def get_user_input():
  answer = ""
  while answer == "":
    answer = input("Please enter a number: ")
  return answer

def convert_to_int(s):
  try:
    print(int(s))
  except ValueError:
    print("Cannot convert to int")

def convert_to_float(s):
  try:
    print(float(s))
  except ValueError:
    print("Cannot convert to float")

def convert_to_decimal(s):
  try:
    print(Decimal(s))
  except DecimalException:
    print("Cannot convert to Decimal")
    
def determine_type(answer):
  return type(answer)

# showing difference in precision of float vs decimal
def diff_decimal_float():
  print("Difference between Decimal and float")
  x = Decimal("0.1")
  y = float("0.1")
  print(f"{x:.20f}")
  print(f"{y:.20f}")

def calc_with_decimals():
  print("Calculating with decimals")
  x = Decimal(34)
  y = Decimal(7)
  z = x / y
  print(f"{z:.20f}")

def calc_with_floats():
  print("Calculating with floats")
  a = 34
  b = 7
  c = a/b
  print(f"{c:.20f}")

def format_number(number):
  print("Formatting alternatives")
  print("{:.2f}".format(number))
  print("{:+.2f}".format(number))
  print("{:.0f}".format(number))
  print("{:0>2d}".format(5))
  print("{:,}".format(1000000))
  print("{:.2%}".format(number))
  print("{:.2e}".format(number))
  print("{:10d}".format(50))
  print("{:<10d}".format(50))
  print("{:^10d}".format(50))

def generate_random_numbers():
  random1 = random.randint(1,6) # 1..6
  random2 = random.randrange(6) # 0..5
  print("Generating random numbers")
  print("With randint: ", random1)
  print("With randrange: ", random2)

def operators_for_ints():
  a = 5
  b = 2
  print("5/2 = %d" % (a/b))
  print("5%%2 = %d" % (a%b))
  print("5//2 = %d" % (a//b))


answer = get_user_input()
print(type(answer))
convert_to_int(answer)
convert_to_float(answer)
convert_to_decimal(answer)
diff_decimal_float()
calc_with_decimals()
calc_with_floats()
format_number(34/7)
generate_random_numbers()
operators_for_ints()


# TODO:
# currency
