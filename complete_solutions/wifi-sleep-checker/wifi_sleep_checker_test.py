import unittest
import datetime
from wifi_sleep_checker import is_time_to_sleep

class SleepTimeTest(unittest.TestCase):
    def test_is_time_to_sleep_false(self):
        date = datetime.datetime.strptime("2017-07-01 15:34", "%Y-%m-%d %H:%M")
        self.assertFalse(is_time_to_sleep(date))

    def test_is_time_to_sleep_true(self):
        date = datetime.datetime.strptime("2017-07-01 23:55", "%Y-%m-%d %H:%M")
        self.assertTrue(is_time_to_sleep(date))


if __name__ == '__main__':
    unittest.main()


