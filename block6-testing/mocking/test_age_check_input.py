#!/usr/bin/python
import unittest
from unittest import mock
from age_check_input import get_user_age 

class TestAgeCheckUserInput(unittest.TestCase):
  def test_user_input(self):
    with mock.patch('builtins.input', return_value=18):
      assert get_user_age() == 18
  
  def test_bad_user_input(self):
    with mock.patch('builtins.input', return_value='test'):
      self.assertRaises(ValueError, get_user_age)

if __name__ == '__main__':
  unittest.main()

