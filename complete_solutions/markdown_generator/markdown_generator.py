#!/usr/bin/python
import sys
from cli_handler import CliHandler
from date_util import DateHandler
from cli_validation_result import ValidationResult
from markdown_format_util import generate_heading
from markdown_format_util import generate_bullet_list

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
  print("Wrting to file %s" % (filename))  
  file = open(filename, "w")
  writeMarkDownHeader(file, title)
  writeFormatting(file)
  file.close()
  print("...file creation completed.")

def writeMarkDownHeader(file, title):
  date_handler = DateHandler()
  file.write(getHeaderDashes())
  file.write(getLayoutString("post"))
  file.write(getTitleString(title))
  file.write(getDateString(date_handler.constructDateString()))
  file.write(getCategoryString("jekyll update"))
  file.write(getHeaderDashes())
  file.write("\n")

def writeFormatting(file):
  print("Writing formatting tips...")
  file.write(generate_heading(1, "heading one"))
  file.write("\n")
  file.write(generate_heading(2, "heading two"))
  file.write("\n")
  file.write(generate_heading(3, "heading three"))
  file.write("\n")
  file.write(generate_bullet_list(create_dummy_list()))

def create_dummy_list():
  bullets = []
  bullets.append("bullet 1")
  bullets.append("bullet 2")
  bullets.append("bullet 3")
  return bullets

if __name__ == '__main__':
  main(sys.argv)
