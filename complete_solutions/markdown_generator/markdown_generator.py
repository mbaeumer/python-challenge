#!/usr/bin/python
import sys
from cli_handler import CliHandler
from date_util import DateHandler

def main(argv):
  cli = CliHandler(argv)
  if cli.isValidArgs():
    writeMarkDownBlogFile(cli.targetFilename, cli.title)

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
