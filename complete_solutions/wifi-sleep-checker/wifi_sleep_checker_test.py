import unittest
import datetime
from wifi_sleep_checker import is_time_to_sleep
from wifi_sleep_checker import get_sleep_datetime

class SleepTimeTest(unittest.TestCase):
    def test_is_time_to_sleep_false(self):
        date = datetime.datetime.strptime("2017-07-01 15:34", "%Y-%m-%d %H:%M")
        sleep_datetime = datetime.datetime.strptime("2017-07-01 23:45", "%Y-%m-%d %H:%M")
        self.assertFalse(is_time_to_sleep(date, sleep_datetime))

    def test_is_time_to_sleep_true(self):
        date = datetime.datetime.strptime("2017-07-01 23:55", "%Y-%m-%d %H:%M")
        sleep_datetime = datetime.datetime.strptime("2017-07-01 23:45", "%Y-%m-%d %H:%M")
        self.assertTrue(is_time_to_sleep(date, sleep_datetime))

    def test_get_sleep_time(self):
        now = datetime.datetime.strptime("2023-03-28 15:34", "%Y-%m-%d %H:%M")
        sleep_timestamp = "22:45"
        expected_sleep_datetime = datetime.datetime.strptime("2023-03-28 22:45", "%Y-%m-%d %H:%M")
        actual_sleep_datetime = get_sleep_datetime(now, sleep_timestamp)

        self.assertEqual(actual_sleep_datetime, expected_sleep_datetime)



if __name__ == '__main__':
    unittest.main()


