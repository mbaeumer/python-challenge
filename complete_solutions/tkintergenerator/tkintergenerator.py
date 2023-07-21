

def get_import():
    return 'from tkinter import *\n'

def get_class_name():
    return 'class Application(Frame):\n'

def get_init_header():
    return 'def __init__(self, master):\n'

def get_init_body():
    body = 'super(Application, self).__init__(master)\n'
    body += get_indent(2) + 'self.grid()\n'
    return body

def get_empty_line():
    return '\n'

def get_main_stuff():
    root_def = 'root = Tk()'
    root_title = 'root.title(\"GUI with OOP\")'
    root_geometry = 'root.geometry(\"200x100\")'
    root_mainloop = 'root.mainloop()'
    result = "\n".join([root_def, root_title, root_geometry, root_mainloop])
    return result



def get_indent(indents):
  result = ""
  index = 0
  single_indent = "  "
  while index < indents:
    result += single_indent
    index = index + 1
  return result

def write_code_to_file():
  filename = 'python_code.py'
  print("Writing class to %s..." % (filename))
  file = open(filename, "w")
  file.write(get_import())
  file.write(get_class_name())
  file.write(get_indent(1))
  file.write(get_init_header())
  file.write(get_indent(2))
  file.write(get_init_body())
  file.write(get_empty_line())
  file.write(get_main_stuff())

if __name__ == '__main__':
  #use a hard-coded filename for starters
  print("Hello")
  write_code_to_file()