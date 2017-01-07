#!/usr/bin/python
from contact import Contact

def print_contacts(contacts):
  for contact in contacts:
    contact.displayContact()

print("Demo of list with non-primitive objects")
print("")

contact = Contact("Martin", "Bäumer", "email", "070707")
contacts = []
contacts.append(contact)
print_contacts(contacts)
