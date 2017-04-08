#!/usr/bin/python
import os

class CliHandler:
  def __init__(self, argv):
    self.cliparams = argv
    self.title = ""
    self.targetFilename = ""

  def isValidArgs(self):

    if len(self.cliparams) < 3:
      return False
    
    self.targetFilename = self.cliparams[1]

    if len(self.cliparams) >= 3:
      index = 2
      while index < len(self.cliparams):
        self.title = self.title + self.cliparams[index] + " "
        index = index + 1
      self.title = self.title[:-1]
    return True
