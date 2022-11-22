import glob
from bean_type import BeanType
from endpoint import Endpoint

# find all Java files
# find all RestControllers, Service, Component
# find all endpoints

def showMenu():
  userinput = ""
  while userinput != "X":
    print("Main menu")
    print("---------")
    print("List all beans - 1")
    print("List all endpoints - 2")
    print("Show bean count - 3")
    print("Exit - X")
    userinput = str(input("Enter your choice: "))


    if userinput == "1":
        all_java_files = find_all_java_files('/Users/martinbaumer/Documents/gitrepo/spring-boot-webclient-sandbox/04_testing_1/src/main/java')
        bean_mapping = find_beans(all_java_files)
        print_beans(bean_mapping)
    elif userinput == "2":
        all_java_files = find_all_java_files('/Users/martinbaumer/Documents/gitrepo/spring-boot-webclient-sandbox/04_testing_1/src/main/java')
        bean_mapping = find_beans(all_java_files)
        endpoints = find_endpoints_per_controller(bean_mapping)
        print_endpoints(endpoints)
    elif userinput == "3":
        all_java_files = find_all_java_files('/Users/martinbaumer/Documents/gitrepo/spring-boot-webclient-sandbox/04_testing_1/src/main/java')
        bean_mapping = find_beans(all_java_files)
        get_bean_counts(bean_mapping)




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
                  bean_type = BeanType.SERVICE
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

def print_beans(bean_mapping):
    for k, v in bean_mapping.items():
        print(k + "-" + str(v))


def get_file_content(filename):
    lines = []
    try:
      with open(filename, 'r') as file:
          for line in file:
              lines.append(line)
    except FileNotFoundError as e:
        print("File could not be found")
    return lines

def find_endpoints_per_controller(bean_mapping):
    endpoints = []
    restcontrollers = find_beans_by_type(bean_mapping, BeanType.CONTROLLER)

    for restcontroller in restcontrollers:
        lines = get_file_content(restcontroller)
        base_url = find_base_url(lines)
        endpoints.extend(find_endpoints(lines, base_url, restcontroller))

    return endpoints


def find_base_url(lines):
    base_url = ""
    line_with_requestmapping = ""
    for line in lines:
        if "@RequestMapping" in line:
            line_with_requestmapping = line
            break
    if len(line_with_requestmapping) > 0:
        start_index = int(line_with_requestmapping.find("(") + 2)
        end_index = int(line_with_requestmapping.find(")") - 1)
        base_url = line_with_requestmapping[start_index:end_index]

    return base_url

def find_endpoints(lines, base_url, restcontroller):
    endpoints = []
    for line in lines:
        if contains_mapping(line):
            http_method = extract_http_method(line)
            url = base_url + extract_url(line)
            endpoints.append(Endpoint(http_method, url, restcontroller))

    return endpoints

def extract_url(line):
    url = ""
    if line.find("(") > 0:
        start_index = int(line.find("(") + 2)
        end_index = int(line.find(")") - 1)
        url = line[start_index:end_index]

    return url


def contains_mapping(line):
    return "@GetMapping" in line or "@PostMapping" in line or "@PutMapping" in line or "@DeleteMapping" in line

def extract_http_method(line):
    http_method = ""
    if "@GetMapping" in line:
        http_method = "GET"
    elif "@PostMapping" in line:
        http_method = "POST"
    elif "@PutMapping" in line:
        http_method = "PUT"
    elif "@DeleteMapping" in line:
        http_method = "DELETE"


    return http_method

def find_beans_by_type(bean_mapping, bean_type):
    filenames = []
    for k,v in bean_mapping.items():
        if v == bean_type:
            filenames.append(k)

    return filenames

def print_endpoints(mapping):
    for e in mapping:
        print(e.displayEndpoint())

def get_bean_counts(bean_mapping):
    controller_counter = 0
    service_counter = 0
    component_counter = 0
    configuration_counter = 0
    for k, v in bean_mapping.items():
        if bean_mapping[k] == BeanType.CONTROLLER:
            controller_counter = controller_counter + 1
        elif bean_mapping[k] == BeanType.SERVICE:
            service_counter = service_counter + 1
        elif bean_mapping[k] == BeanType.COMPONENT:
            component_counter = component_counter + 1
        elif bean_mapping[k] == BeanType.CONFIGURATION:
            configuration_counter = configuration_counter + 1


    print("Bean counts")
    print("Number of controllers: \t %d" % (controller_counter))
    print("Number of services: \t %d" % (service_counter))
    print("Number of components: \t %d" % (component_counter))
    print("Number of configuration: \t %d" % (configuration_counter))




if __name__ == '__main__':
    showMenu()

