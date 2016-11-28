import unittest
from sum_function import sum

class SumTestCase(unittest.TestCase):
  def test_sum(self):
    self.assertTrue(sum(5,5)==10)

if __name__ == '__main__':
  unittest.main()
