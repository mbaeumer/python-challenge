#!/usr/bin/python

def get_python_path():
  return "#!/usr/bin/python\n"

def get_import_unittest():
  return "import unittest\n"

def get_testclass_header(class_name):
  if class_name != "":
    result = "class %s(unittest.TestCase):" % (class_name)
    result += "\n"
    return result
  else:
    raise ValueError

def get_test_method_header(method_name):
  result = "def %s(self):\n" % (method_name)
  return result

def get_self_assertTrue():
  result = "self.assertTrue()\n"
  return result

def indent(indents):
  result = ""
  index = 0
  single_indent = "  "
  while index < indents:
    result += single_indent
    index = index + 1
  return result

def get_main_header():
  return "if __name__ == '__main__'\n"

def create_comment(comment):
  result = "#"
  result += comment

def get_main_body():
  return "unittest.main()"
