#!/usr/bin/python

class Contact:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname

  def displayContact(self):
    print("Firstname: %s, lastname: %s" % (self.firstname, self.lastname))


print("A simple demo of OOP in python")
print("")

print("Creating a contact...")
contact = Contact("Martin", "Bäumer")

print("Printing the contact details...")
contact.displayContact()

  
