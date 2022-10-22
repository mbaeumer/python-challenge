#!/usr/bin/python
import os
import glob

def main():
  print_info()
  show_dir_content()
  show_file_type(os.getcwd())
  #create_backup_directory("backup")
  show_file_type("data")
  rename_file("data/data1.txt", "data/data2.txt")
  show_file_type("data")
  print(get_file_extension("source_text.txt"))
  walk_files_in_dir("parent_folder")
  walk_files_with_filetype_in_dir("parent_folder", "py")

def print_info():
  print("Demo of file operations in python")
  print("")

def show_dir_content():
  print("The current working directory: %s" % (os.getcwd()))
  print("...iterating through a directory and find all files")
  dir_content = os.listdir(os.getcwd())
  for file in dir_content:
    print(file)

def show_file_type(directory):
  dir_content = os.listdir(directory)
  print("Content of directory: %s" % (directory))
  for file in dir_content:
    print("Filename: %s, type: %s " % (file, getDirOrFile(file))) 

def getDirOrFile(file):
  result = "file"
  if os.path.isdir(file):
    result = "directory"
  return result

def check_if_file_exists(filename):
  if os.path.isfile(filename):
    print("The file %s exists" % (filename))
  else:
    print("The file %s does not exist" % (filename))

def create_backup_directory(directory):
  if not os.path.exists(directory):
    os.makedirs(directory)
  else:
    print("The directory %s already exists" % (directory))

#def copy_file(source, target):

def rename_file(old_name, new_name):
  print("renaming a file...")
  if not os.path.isfile(old_name):
    print("The file %s does not exist and cannot be renamed" % (old_name))
    return

  os.rename(old_name, new_name)
  #if os.path.exists(new_name):
    #print("The file %s was renamed to %s" % (old_name, new_name))

def delete_file(filename):
  print("...deleting a file")
  if os.path.isfile(filename):
    os.remove(filename)
    print("The file %s has been deleted" % (filename))
  else:
    print("The file %s does not exist" % (filename))

def get_file_stats():
  print("Retrieving file stats")
  filename = "source_folder/source_text.txt"
  statresult = os.stat(filename)
  print(statresult.st_size)

def get_file_extension(filename):
  print("get file extension")
  return os.path.splitext(filename)[1]

def walk_files_in_dir(base_dir):
  files = glob.glob(base_dir + '/**/*.*', recursive=True)
  for file in files:
    print(file)

def walk_files_with_filetype_in_dir(base_dir, extension):
  files = glob.glob(base_dir + '/**/*.' + extension, recursive=True)
  for file in files:
    print(file)

if __name__ == '__main__':
  main()
