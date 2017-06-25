#!/usr/bin/python
from status import Status

print("Demo of enums in python")
print("")

print("Step 1: creating a variable of type Status with value OPEN")
status  = Status.OPEN
print("Status: " + str(status))

print("Step 2: Setting the status with a numeric value")
another_status = Status(2)
print(another_status)

print("Step 2: checking the value of the enum variable...")
if status == Status.COMPLETED:
  print("Congrats, the task is completed")
else:
  print("Sorry, the task is not completed yet")

print("Step 3: See all available values for the enumeration status...")
for status in Status:
  print(status)

print("Step 4: accessing the enum by numeric value: Status(1)")
print(Status(1))
print("Step 5: accessing an enum value that does not exist: Status(4) should not exist")
try:
  print(Status(4))
except ValueError:
  print("Status(4) is not valid!")

print("Step 6: checking if a potential member is really a member of an enum...")
print(isinstance(Status.OPEN, Status))

print("Step 7: Retrieving the value of an enum member...")
print("Status.OPEN has the numeric value %d " % (Status.OPEN.value))
