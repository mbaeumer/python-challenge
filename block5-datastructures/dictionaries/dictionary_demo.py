#!/usr/bin/python

def print_dictionary(thedictionary):
  for k, v in thedictionary.items():
    print(k, v)

print("Demo of dictionary")
print("")

# create a dictionary
conversion_rates = {}

# add an entry
conversion_rates['us'] = 0.11
conversion_rates['eu'] = 0.10
conversion_rates['ch'] = 0.11

# looping
print("following conversion rates are available: ")
print_dictionary(conversion_rates)

# checking if a key exists
key = input("Enter a key to check if it exists: ")
if (key in conversion_rates):
  print("the key '%s' exists" % (key))
  print("The value is: %f" % (conversion_rates[key]))
else:
  print("the key '%s' does not exist" % (key))
