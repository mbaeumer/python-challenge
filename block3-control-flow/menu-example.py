#!/usr/bin/python

def showMenu():
  userinput = ""
  while userinput != "X":
    print("Main menu")
    print("---------")
    print("Create - 1")
    print("View all - 2")
    print("Delete - 3")
    print("Exit - X")
    userinput = input("Enter your choice: ")


print("Example of a while loop using a simple menu")
print("")
showMenu()
