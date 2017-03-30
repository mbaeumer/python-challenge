#!/usr/bin/python
import sys

def main(argv):
  if validateCliArgs(argv):
    writeMarkDownBlogFile(argv[1], argv[2])

def validateCliArgs(argv):
  if len(argv) < 3:
    print("Sorry, you have not provided the correct arguments!")
    return False
  targetFileName = str(argv[1])
  if not targetFileName.endswith(".markdown"):
    print("The filename '%s' is not correct!" % (targetFileName))
    return False
  return True

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
