#!/usr/bin/python

class Contact:
  def __init__(self, firstname, lastname, email, phone):
    self.firstname = firstname
    self.lastname = lastname
    self.email = email
    self.phone = phone
  
  def displayContact(self):
    print("%s, %s, %s, %s" % (self.firstname, self.lastname, self.email, self.phone))

