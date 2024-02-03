import unittest
from leap_year import is_leap_year

class SumTestCase(unittest.TestCase):
  def test_2000(self):
    self.assertTrue(is_leap_year(2000))

  def test_1996(self):
    self.assertTrue(is_leap_year(1996))

  def test_1700(self):
    self.assertFalse(is_leap_year(1700))


if __name__ == '__main__':
  unittest.main()