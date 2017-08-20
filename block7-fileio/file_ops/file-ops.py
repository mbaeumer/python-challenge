#!/usr/bin/python
import os


print("Example of file operations in python")
print("")
print("...checking if a file exists")

filename = "source_text.txt"
if os.path.isfile(filename):
  print("The file %s exists" % (filename))
else:
  print("The file %s does not exist" % (filename))

filename = "source_folder/source_text.txt"
if os.path.exists(filename):
  print("The file %s exists" % (filename))
else:
  print("The file does %s not exist" % (filename))

print("renaming a file...")
new_file_name = "source_folder/source_text2.txt"
os.rename(filename, new_file_name)
if os.path.exists(new_file_name):
  print("The file %s was renamed to %s" % (filename, new_file_name))

print("...and changing the file name back...")
os.rename(new_file_name, filename)
if os.path.exists(filename):
  print("The file %s was again renamed to %s" % (new_file_name, filename))

print("...deleting a file")
filename = "file_to_delete.txt"
if os.path.isfile(filename):
  os.remove(filename)
  print("The file %s has been deleted" % (filename))
else:
  print("The file %s does not exist" % (filename))

print("...creating a folder")
directory = "temp"
if not os.path.exists(directory):
  os.makedirs(directory)
else:
  print("The directory %s already exists" % (directory))
