#!/usr/bin/python
from person import Person

def read_csv_file(filename):
  persons = []
  try:
    file = open(filename, "r")
    i = 0
    for line in file:
      i = i + 1
      line = line[:-1]
      splitted = line.split(",")
      person = Person(splitted[1], splitted[0], splitted[2])
      persons.append(person)
    file.close()
  except FileNotFoundError:
    raise FileNotFoundError
  return persons
