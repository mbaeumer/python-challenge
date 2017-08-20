#!/usr/bin/python
from csvreader import read_csv_file
from parsestats import ParseStats

def main():
  print_title()
  persons = read_file()
  prepare_format(persons)
  ps = prepare_format(persons)
  print_result(ps, persons) 
 
def print_title():
  print("Demo of eading csv-files")
  print("")

def read_file():
  persons = []
  try:
    filename = "persons.csv"
    persons = read_csv_file(filename)
  except FileNotFoundError:
    print("The file does not exist")
  return persons

def prepare_format(persons):
  max_first = 0
  max_last = 0
  for p in persons:
    if len(p.firstname) > max_first:
      max_first = len(p.firstname)
    if len(p.lastname) > max_last:
      max_last = len(p.lastname)
  ps = ParseStats(max_first, max_last)
  return ps

def print_result(ps, persons):
  last_header = "Last"
  last_header = adjust_length(last_header, ps.last)

  first_header = "First"
  first_header = adjust_length(first_header, ps.first)  
  
  salary_header = "Salary"
  print("%s %s %s" % (last_header, first_header, salary_header))
  total = last_header + first_header + salary_header
  line = ""
  for char in total:
    line = line + "-"
  print(line)
  for p in persons:
    p.lastname = adjust_length(p.lastname, ps.last)
    p.firstname = adjust_length(p.firstname, ps.first)
    p.salary = get_as_currency(float(p.salary))
    print("%s %s %s" % (p.lastname, p.firstname, p.salary))

def get_as_currency(value):
  return '{:,.2f}$'.format(value)

def adjust_length(text, max):
  index = len(text)
  while index < max:
    text = text + " "
    index = index + 1
  return text
if __name__ == '__main__':
  main()
