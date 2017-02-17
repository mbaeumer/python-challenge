#!/usr/bin/python
import sys
import tg_core

def main(argv):
  if validateArguments(argv):
    print("Provided arguments OK...")
    writeFile(argv[1], argv[2])
  else:
    print(create_usage()) 

def validateArguments(argv):
  if len(argv) != 3:
    print("Sorry! You have not provided enough args.")
    return False
  filename = str(argv[1])
  if not filename.endswith(".py"):
    print("The given filename is not correct")
    return False
  return True

def create_usage():
  result = "Usage:\n"
  result += "arg1: filename"
  return result

def writeFile(filename, classname):
  print("Writing test class '%s' to %s..." % (classname, filename))
  file = open(filename, "w")
  file.write(tg_core.get_python_path())
  file.write(tg_core.get_import_unittest())
  file.write(tg_core.get_testclass_header(classname))
  file.write(tg_core.indent(1))
  file.write(tg_core.get_test_method_header("test_something"))
  file.write(tg_core.indent(2))
  file.write(tg_core.get_self_assertTrue())
  file.write(tg_core.get_main_header())
  file.write(tg_core.indent(1))
  file.write(tg_core.get_main_body())
  file.close()
  print("...file created")

if __name__ == '__main__':
  main(sys.argv)
