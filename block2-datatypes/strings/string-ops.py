#!/usr/bin/python

print("Demo of string operations")

def some_classic_string_ops():
  print("")
  lorem = "lorem ipsum"
  print("Dummy string:  ", lorem)
  print("Length: ",len(lorem) )
  print("Capitalized: " + lorem.capitalize())
  print("endswith 'ipsum': " + str(lorem.endswith("ipsum")))
  print("islower: " + str(lorem.islower()))
  print("isnumeric: " + str(lorem.isnumeric()))
  print("isalpha: " + str(lorem.isalpha()))
  print("isspace: " + str(lorem.isspace()))

def string_equality():
  lorem="lorem ipsum"
  lorem2 = "lorem ipsum"
  print("Testing for string equality (case_sensitive)")
  if lorem == lorem2:
    print("The strings are equal")
  else:
    print("The strings are not equal")

  lorem2 = "Lorem ipsum"
  print("Testing for string equality (case-insensitive)")
  if lorem.lower() == lorem2.lower():
    print("The strings are equal")
  else:
    print("The strings are not equal")

def string_contains_character():
  lorem = "lorem ipsum"
  print("Checking if a string contains certain characters:")
  print("m" in lorem)
  print("a" in lorem)

def substring_index_in_string():
  lorem = "Lorem ipsum"
  print("Checking at which index a certain substring appears")
  print("lorem", lorem.find("lorem"))
  print("rem", lorem.find("rem"))
  print("ips", lorem.find("ips"))
  print("abc", lorem.find("abc"))

  print("Checking how often a substring appears:")
  teststring = "abbaaaa"
  print(teststring)
  print(teststring.count("aa"))

def string_iterate():
  lorem = "Lorem ipsum"
  print("Iterate through a string")
  for c in lorem:
    print(c)
  print("")
  i = 0
  while i < len(lorem):
    print(lorem[i])
    i = i + 1

def string_split():
  lorem = "Lorem ipsum"
  print("Splitting a string")
  splitted = lorem.split(" ")
  for word in splitted:
    print(word)

def remove_character_from_string():
  lorem = "Lorem ipsum"
  print("Removing a character in a string")
  new_lorem = lorem.replace("m", "")
  print("new string after removal: %s" % (new_lorem))

def insert_character_in_string():
  lorem = "Lorem ipsum"
  print("Inserting a character into a string")
  new_lorem = lorem[:5] + "-" + lorem[6:]
  print("new string after modification: %s" % (new_lorem))

def use_not_operator():
  print("Using the not operator")
  name=""
  if not name:
    print("the name is not set")

  name="abc"
  if not name:
    print("the name is still not set")
  else:
    print("now the name is set")

def use_string_indices():
  print("Experiment")
  lorem = "Lorem ipsum"
  print(lorem)
  print("lorem[1] >> %s" % (lorem[1]))
  print("lorem[10] >> %s" % (lorem[10]))
  print("lorem[1:] >> %s" % (lorem[1:]))
  print("lorem[5:] >> %s" % (lorem[5:]))
  print("lorem[:1] >> %s" % (lorem[:1]))
  print("lorem[:6] >> %s" % (lorem[:6]))
  print("lorem[:8] >> %s" % (lorem[:8]))
  print("lorem[1:3] >> %s" % (lorem[1:3]))

def use_strip():
  lorem = "  Lorem ipsum  "
  print("original string: %s" % (lorem))
  print("after strip: %s" % (lorem.strip()))

def create_binary_array():
  binary_lorem = b"Lorem ipsum"
  print(binary_lorem)
  print(binary_lorem[0])
  return binary_lorem

def binary_to_string(binary):
  print(binary.decode())
  return binary.decode()

def string_to_binary(string):
  print("string parameter: %s" % (string))
  print(string.encode())


  
if __name__ == '__main__':
  some_classic_string_ops()
  string_equality()
  string_contains_character()
  substring_index_in_string()
  string_iterate()
  string_split()
  remove_character_from_string()
  insert_character_in_string()
  use_not_operator()
  use_string_indices()
  use_strip()
  binary = create_binary_array()
  string = binary_to_string(binary)
  string_to_binary(string)
