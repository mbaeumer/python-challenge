#!/usr/bin/python
import sys
from cli_handler import CliHandler

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
  print("Wrting to file %s" % (filename))  
  file = open(filename, "w")
  file.write(getHeaderDashes())
  file.write(getLayoutString("post"))
  file.write(getTitleString(title))
  file.write(getDateString("2017-03-28 22:00:00"))
  file.write(getCategoryString("jekyll update"))
  file.write(getHeaderDashes())
  file.close()
  print("...file creation completed.")

if __name__ == '__main__':
  main(sys.argv)
