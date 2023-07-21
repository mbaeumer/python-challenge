import unittest
import datetime
from age_calculator import calculate_age

class SumTestCase(unittest.TestCase):
  def test_calculate_age_one_day_before(self):
    birth_date = datetime.datetime.strptime("1981-07-23", "%Y-%m-%d")
    today = datetime.datetime.strptime("2023-07-22", "%Y-%m-%d")
    self.assertEqual(calculate_age(today, birth_date),41)

  def test_calculate_age_equals(self):
    birth_date = datetime.datetime.strptime("1981-07-22", "%Y-%m-%d")
    today = datetime.datetime.strptime("2023-07-22", "%Y-%m-%d")
    self.assertEqual(calculate_age(today, birth_date),42)

  def test_calculate_age_already_had_birthday(self):
    birth_date = datetime.datetime.strptime("1981-07-15", "%Y-%m-%d")
    today = datetime.datetime.strptime("2023-07-22", "%Y-%m-%d")
    self.assertEqual(calculate_age(today, birth_date),42)


if __name__ == '__main__':
  unittest.main()
