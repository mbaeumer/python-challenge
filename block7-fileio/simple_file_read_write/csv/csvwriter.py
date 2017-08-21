#!/usr/bin/python
from person import Person

def write_csv_file(filename, persons):
  try:
    file = open(filename, "w")
    for p in persons:
      line = p.lastname + "," + p.firstname + "," + str(p.salary) + "\n"
      file.write(line)
    file.close()
    print("Finished writing data to file")
  except FileNotFoundError:  
    raise FileNotFoundError


