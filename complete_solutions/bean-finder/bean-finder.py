import glob
from bean_type import BeanType

# find all Java files
# find all RestControllers, Service, Component
# find all endpoints

def find_all_java_files(base_dir):
    java_files = []
    files = glob.glob(base_dir + '/**/*.java', recursive=True)
    for file in files:
        java_files.append(file)
        print(file)
    return java_files

def get_bean_type(filename):
    bean_type = BeanType.NONE
    try:
      with open(filename, 'r') as file:
          for line in file:
              if "@RestController" in line:
                  bean_type = BeanType.CONTROLLER
              elif "@Service" in line:
                  bean_type = BeanType.CONTROLLER
              elif "@Component" in line:
                  bean_type = BeanType.COMPONENT
              elif "@Configuration" in line:
                  bean_type = BeanType.CONFIGURATION
    except FileNotFoundError as e:
        print("File could not be found")
    return bean_type

def find_beans(java_files):
    bean_type_dict = {}
    for file in java_files:
        bean_type_dict[file] = get_bean_type(file)
    return bean_type_dict

def get_file_content(filename):
    lines = []
    try:
      with open(filename, 'r') as file:
          for line in file:
              lines.append(line)
    except FileNotFoundError as e:
        print("File could not be found")
    return lines

def find_endpoints(bean_mapping):
    endpoints = []
    restcontrollers = find_beans_by_type(bean_mapping, BeanType.CONTROLLER)

    for restcontroller in restcontrollers:
        lines = get_file_content(restcontroller)
        base_url = find_base_url(lines)
        


def find_base_url(lines):
    base_url = ""
    line_with_requestmapping = ""
    for line in lines:
        if "@RequestMapping" in line:
            line_with_requestmapping = line
            break
    if len(line_with_requestmapping) > 0:
        base_url = [line_with_requestmapping.find("("), line_with_requestmapping.find(")")]

    return base_url

def find_beans_by_type(bean_mapping, bean_type):
    filenames = []
    for k,v in bean_mapping.items():
        if v == bean_type:
            filenames.append(k)

    return filenames





if __name__ == '__main__':
    all_java_files = find_all_java_files('/Users/martinbaumer/Documents/gitrepo/spring-boot-webclient-sandbox/04_testing_1/src/main/java')
    bean_mapping = find_beans(all_java_files)