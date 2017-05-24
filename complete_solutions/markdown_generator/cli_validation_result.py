#!/usr/bin/python
from enum import Enum

class ValidationResult(Enum):
  OK = 1
  HELP = 2
  NOT_ENOUGH_ARGS = 3

