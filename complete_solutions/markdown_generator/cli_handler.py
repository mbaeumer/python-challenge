#!/usr/bin/python
import os
import re
from cli_validation_result import ValidationResult

class CliHandler:
  def __init__(self, argv):
    self.cliparams = argv
    self.title = ""
    self.targetFilename = ""

  def matchesFormat(self):
    return re.match(r'^...', self.targetFilename)

  def isValidArgs(self):
    if len(self.cliparams) == 2 and self.cliparams[1] == "-help":
      return ValidationResult.HELP
    if len(self.cliparams) < 2:
      return ValidationResult.NOT_ENOUGH_ARGS
    if len(self.cliparams) == 2:
      self.targetFilename = self.cliparams[1]
      return ValidationResult.OK
    
    #if self.targetName
    if len(self.cliparams) >= 3:
      index = 2
      while index < len(self.cliparams):
        self.title = self.title + self.cliparams[index] + " "
        index = index + 1
      self.title = self.title[:-1]
    return ValidationResult.OK
