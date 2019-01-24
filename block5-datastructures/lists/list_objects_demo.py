#!/usr/bin/python
from contact import Contact

def print_contacts(contacts):
  for contact in contacts:
    contact.displayContact()

def print_contacts_comprehension(contacts):
  [contact.displayContact() for contact in contacts]  

def find_contacts_with_phone_contains_1(contacts):
  [contact.displayContact() for contact in contacts if "1" in contact.phone]

def create_contact(firstname, lastname, mail, phone):
  contact = Contact(firstname, lastname, mail, phone)
  return contact


print("Demo of list with non-primitive objects")
print("")

print("\nInitializing a list")
contacts = []
contacts.append(create_contact("Martin", "Bäumer", "mail",  "0786777566"))
contacts.append(create_contact("Bob", "Marley", "mail",  "071666224"))
contacts.append(create_contact("Jane", "Doe", "mail",  "01356867566"))
contacts.append(create_contact("Laurel", "Aitken", "mail",  "983444566"))

print("\nPrinting the content of the list")
print_contacts(contacts)

print("\nIterating through the content of the list using comprehension")
print_contacts_comprehension(contacts)

print("\nSorting the list based on the first name ")
sorted_list = sorted(contacts, key=lambda x: x.firstname, reverse=False)
print_contacts_comprehension(sorted_list)

print("\nDeleting the last contact from the list")
del contacts[3]
print_contacts_comprehension(contacts)

print("\nFiltering a list based on a criteria")
find_contacts_with_phone_contains_1(sorted_list)

