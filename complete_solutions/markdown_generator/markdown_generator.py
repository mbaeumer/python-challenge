#!/usr/bin/python
import sys
from cli_handler import CliHandler
from date_util import DateHandler
from cli_validation_result import ValidationResult

def print_usage():
  print("Usage:")
  print("--------------")
  print("[1]: the target file name")
  print("[2]: the title of the blog post (optional)")

def main(argv):
  cli = CliHandler(argv)
  if cli.isValidArgs() == ValidationResult.OK:
    writeMarkDownBlogFile(cli.targetFilename, cli.title)
  elif cli.isValidArgs() == ValidationResult.NOT_ENOUGH_ARGS:
    print("ERROR: You have not provided enough arguments!")
    print("Use -help to find out more about the usage...")  
  elif cli.isValidArgs() == ValidationResult.HELP:
    print_usage()
  elif cli.isValidArgs() == ValidationResult.NOT_PYTHON:
    print("ERROR: The target file should be a python file!")  
    
def getHeaderDashes():
  return "---\n"

def getLayoutString(layout):
  return "layout: " + layout + "\n"

def getTitleString(title):
  return "title: " + "\"" + title + "\"" "\n"

def getDateString(date):
  return "date: " + date + "\n"

def getCategoryString(category):
  return "categories: " + category + "\n"

def writeMarkDownBlogFile(filename, title):
  date_handler = DateHandler()
  print("Wrting to file %s" % (filename))  
  file = open(filename, "w")
  file.write(getHeaderDashes())
  file.write(getLayoutString("post"))
  file.write(getTitleString(title))
  file.write(getDateString(date_handler.constructDateString()))
  file.write(getCategoryString("jekyll update"))
  file.write(getHeaderDashes())
  file.close()
  print("...file creation completed.")

if __name__ == '__main__':
  main(sys.argv)
