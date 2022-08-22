import unittest
from list_group_items import group_items

class GroupItemTestCase(unittest.TestCase):
    def test_group_items(self):
        list = ['A', 'B', 'C', 'B', 'B', 'C', 'B', 'A']

        result = group_items(list)
        self.assertTrue('A' in result)
        countA = result['A']
        self.assertEqual(countA, 2)
        countB = result['B']
        self.assertEqual(countB, 4)


if __name__ == '__main__':
    unittest.main()