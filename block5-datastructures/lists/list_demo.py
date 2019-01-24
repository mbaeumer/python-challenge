#!/usr/bin/python

print("Demo of some basic list operations")
print("")

def print_list(names):
  for name in names:
    print("%s" % (name))
  print("-----END OF LIST------")

names = []
names.append("Martin")

print_list(names)
print("list content after insert")
names.insert(0, "Kalle")
print_list(names)

del names[0]
print("list content after del")
print_list(names)

if names.count("Joe") > 0:
  names.remove("Joe")

names.append("Bill")
names.append("Lotta")
names.append("Paul")

print_list(names)

names.sort()
print_list(names)

del names[1]
print_list(names)

print("Getting the size of the list")
print(len(names))
