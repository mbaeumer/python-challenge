#!/usr/bin/python
print("Demo of for loops")
print("")

word = "hello"
for letter in word:
  print(letter)

print("Counting using range")
for i in range(10):
  print(i, end=" ")
print("")

print("Counting in steps")
for i in range(0,10,2):
  print(i, end=" ")
print("")

print("Counting backwards")
for i in range(10,0,-1):
  print(i, end=" ")
print("")

