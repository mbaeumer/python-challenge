#!/usr/bin/python
from status import Status

print("Demo of enumms in python")
print("")

print("Step 1: creating a variable of type Status...")
status  = Status.OPEN
print("Status: " + str(status))

print("Step 2: checking the value of the enum variable...")
if status == Status.COMPLETED:
  print("Congrats, the task is completed")
else:
  print("Sorry, the task is not completed yet")

print("Step 3: See all available values for the enumeration status...")
for status in Status:
  print(status)

print("Step 4: accessing the enum by value...")
print(Status(1))
print("Step 5: accessing an enum value that does not exist...")
#print(Status(4))
print("Step 6: checking if a potential member  is really a member of an enum...")
print(isinstance(Status.OPEN, Status))
print("Step 7: Retrieving the value of an enum member...")
print("Status.OPEN has the value %d " % (Status.OPEN.value))
