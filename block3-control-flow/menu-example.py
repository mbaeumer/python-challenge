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

def show_alternative_menu():
  menu_options = {
    1: 'Create',
    2: 'View all',
    3: 'Delete',
    4: 'Exit'
  }

  while (True):
    for key in menu_options.keys():
      print(key, '-', menu_options[key])
    userinput = int(input("Enter your choice: "))
    if userinput == 4:
      break

print("Example of a while loop using a simple menu")
print("")
showMenu()
show_alternative_menu()
