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

# checking if an entry exists
print('eu' in conversion_rates)
print('no' in conversion_rates)
