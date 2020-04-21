#!/usr/bin/python

print("Demo of string operations")
print("")
lorem = "lorem ipsum"
print("Dummy string:  ", lorem)
print("Length: ",len(lorem) )
print("Capitalized: " + lorem.capitalize())
print("endswith 'ipsum': " + str(lorem.endswith("ipsum")))
print("islower: " + str(lorem.islower()))
print("isnumeric: " + str(lorem.isnumeric()))
print("isspace: " + str(lorem.isspace()))

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


print("Checking if a string contains certain characters:")
print("m" in lorem)
print("a" in lorem)

print("Checking at which index a certain substring appears")
print("lorem", lorem.find("lorem"))
print("rem", lorem.find("rem"))
print("ips", lorem.find("ips"))
print("abc", lorem.find("abc"))

print("Checking how often a substring appears:")
teststring = "abbaaaa"
print(teststring)
print(teststring.count("aa"))

print("Iterate through a string")
for c in lorem:
  print(c)
print("")
i = 0
while i < len(lorem):
  print(lorem[i])
  i = i +1

print("Splitting a string")
splitted = lorem.split(" ")
for word in splitted:
  print(word)

print("Removing a character in a string")
new_lorem = lorem.replace("m", "")
print("new string after removal: %s" % (new_lorem))

print("Inserting a character into a string")
new_lorem = lorem[:5] + "-" + lorem[6:]
print("new string after modification: %s" % (new_lorem))

print("Using the not operator")
name=""
if not name:
  print("the name is not set")
name="abc"
if not name:
  print("the name is still not set")
else: 
  print("now the name is set")
  
