#!usr/bin/python
import unittest
from simple_math_lib import sum
from simple_math_lib import subtract

class SimpleMathLibTest(unittest.TestCase):
  def test_sum(self):
    self.assertTrue(sum(5,5) == 10)

  def test_subtract(self):
    self.assertTrue(subtract(10,5) == 5)

if __name__ == '__main__':
  unittest.main()
